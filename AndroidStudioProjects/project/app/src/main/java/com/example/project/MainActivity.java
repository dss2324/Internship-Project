package com.example.project;

import static android.content.ContentValues.TAG;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.Toast;
import android.widget.PopupMenu;
import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.core.content.FileProvider;

import com.bumptech.glide.Glide;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    private LinearLayout imagesLayout;
    private final ActivityResultLauncher<Intent> cameraLauncher = registerForActivityResult(
            new ActivityResultContracts.StartActivityForResult(),
            result -> {
                if (result.getResultCode() == RESULT_OK) {
                    if (result.getData() != null && result.getData().hasExtra("imagePath")) {
                        String imagePath = result.getData().getStringExtra("imagePath");
                        Log.d(TAG, "Image path received from camera: " + imagePath);
                        // Add image to view
                        addImageView(imagePath);
                        // Save the image path to SharedPreferences
                        saveImagePathToPreferences(imagePath);

                    }
                }
            }
    );

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        imagesLayout = findViewById(R.id.images_layout);
        setupFileDirectory();
        // Load and display images from SharedPreferences
        loadAndDisplayImages();

        Button openCustomCameraButton = findViewById(R.id.openCustomCameraButton);
        openCustomCameraButton.setOnClickListener(v -> openCustomCamera());
    }

    private void loadAndDisplayImages() {
        SharedPreferences sharedPreferences = getSharedPreferences("MyAppPrefs", MODE_PRIVATE);
        Gson gson = new Gson();
        String imageUriListJson = sharedPreferences.getString("imageUriList", "[]");
        List<String> imageUriList = gson.fromJson(imageUriListJson, new TypeToken<List<String>>() {}.getType());

        for (String imageUriString : imageUriList) {
            addImageView(imageUriString);
        }
    }

    private void addImageView(String imagePath) {
        LinearLayout imageContainer = findViewById(R.id.images_layout);

        Log.d(TAG, "Adding image with path: " + imagePath);

        Uri imageUri = Uri.parse(imagePath);
        File imageFile = new File(imageUri.getPath());

        if (!imageFile.exists()) {
            Log.e(TAG, "File does not exist: " + imagePath);
            return;
        }

        boolean imageExists = false;
        for (int i = 0; i < imageContainer.getChildCount(); i++) {
            ConstraintLayout imageWrapper = (ConstraintLayout) imageContainer.getChildAt(i);
            ImageView imageView = (ImageView) imageWrapper.getChildAt(0); // Assuming the first child is the ImageView

            if (imageView != null) {
                String tag = (String) imageView.getTag();
                if (tag != null && tag.equals(imagePath)) {
                    imageExists = true;
                    Log.d(TAG, "Image already exists in container: " + imagePath);
                    return;
                }
            } else {
                Log.e(TAG, "ImageView not found in imageWrapper.");
            }
        }

        if (!imageExists) {
            // Create ConstraintLayout
            ConstraintLayout imageWrapper = new ConstraintLayout(this);
            LinearLayout.LayoutParams layoutParams = new LinearLayout.LayoutParams(
                    LinearLayout.LayoutParams.MATCH_PARENT,
                    LinearLayout.LayoutParams.WRAP_CONTENT
            );
            layoutParams.setMargins(10, 10, 10, 10);
            imageWrapper.setLayoutParams(layoutParams);

            // Create ImageView
            ImageView imageView = new ImageView(this);
            imageView.setId(View.generateViewId()); // Generate unique ID
            imageView.setTag(imagePath);

            ConstraintLayout.LayoutParams imageParams = new ConstraintLayout.LayoutParams(
                    400, // Use constraints for width
                    400 // Fixed height; adjust as needed
            );
            imageParams.startToStart = ConstraintLayout.LayoutParams.PARENT_ID;
            imageParams.topToTop = ConstraintLayout.LayoutParams.PARENT_ID;
            imageParams.endToStart = View.generateViewId(); // Reference ID for spinner icon
            // Fixed width; adjust as needed
            imageParams.topMargin=20;
            imageView.setLayoutParams(imageParams);
            imageView.setScaleType(ImageView.ScaleType.CENTER_CROP); // Maintain aspect ratio
            Glide.with(this).load(imageUri).error(R.drawable.error_image).into(imageView);
            imageView.setOnClickListener(v -> {
                Intent intent = new Intent(MainActivity.this, ImageDetailsActivity.class);
                intent.putExtra("imageUri", imageUri.toString());
                startActivity(intent);
            });

            // Create Spinner Icon
            ImageView spinnerIcon = new ImageView(this);
            int spinnerIconId = View.generateViewId(); // Generate unique ID for the spinner icon
            spinnerIcon.setId(spinnerIconId);
            spinnerIcon.setImageResource(R.drawable.ic_spinner);

            ConstraintLayout.LayoutParams spinnerParams = new ConstraintLayout.LayoutParams(
                    70,
                    70
            );
            spinnerParams.endToEnd = ConstraintLayout.LayoutParams.PARENT_ID;
            spinnerParams.topToTop = ConstraintLayout.LayoutParams.PARENT_ID;
            spinnerParams.bottomToBottom = ConstraintLayout.LayoutParams.PARENT_ID;
            spinnerParams.startToEnd = imageView.getId(); // Position spinner icon to the right of the image
            spinnerParams.leftMargin=0; // Margin between image and spinner icon
            spinnerIcon.setLayoutParams(spinnerParams);
            spinnerParams.topToTop=3;
            spinnerIcon.setOnClickListener(v -> showPopupMenu(v, imagePath));

            // Add Views to ConstraintLayout
            imageWrapper.addView(imageView);
            imageWrapper.addView(spinnerIcon);

            // Add ConstraintLayout to LinearLayout
            imageContainer.addView(imageWrapper);
            Log.d(TAG, "Adding new image to container: " + imagePath);
        }
        Log.d(TAG, "Number of images in container after adding: " + imageContainer.getChildCount());
    }

    private void showPopupMenu(View view, String imagePath) {
        PopupMenu popupMenu = new PopupMenu(this, view);
        popupMenu.getMenuInflater().inflate(R.menu.image_popup_menu, popupMenu.getMenu());

        popupMenu.setOnMenuItemClickListener(menuItem -> {
          if (menuItem.getItemId() == R.id.action_delete) {
                deleteImage(imagePath);
                removeImagePathFromPreferences(imagePath);
                return true;
            } else {
                return false;
            }
        });
        popupMenu.show();
    }

    private Uri getUriForFile(String imagePath) {
        File imageFile = new File(imagePath);
        Log.d(TAG, "File path: " + imagePath);
        if (imageFile.exists()) {
            Uri uri = FileProvider.getUriForFile(this, "com.example.project.fileprovider", imageFile);
            Log.d(TAG, "File URI: " + uri.toString());
            return uri;
        } else {
            Log.e(TAG, "File does not exist: " + imagePath);
            return null;
        }
    }








    // Example in initialization or setup method
    private void setupFileDirectory() {
        File cacheDir = getCacheDir();
        File imageDir = new File(cacheDir, "images");
        if (!imageDir.exists()) {
            imageDir.mkdirs(); // Create directory if it does not exist
        }
        // Proceed to use imageDir for storing or accessing files
    }


    private void deleteImage(String imagePath) {
        LinearLayout imageContainer = findViewById(R.id.images_layout);
        for (int i = 0; i < imageContainer.getChildCount(); i++) {
            ConstraintLayout imageWrapper = (ConstraintLayout) imageContainer.getChildAt(i);
            ImageView imageView = (ImageView) imageWrapper.getChildAt(0); // Assuming the first child is the ImageView

            if (imageView != null) {
                String tag = (String) imageView.getTag();
                if (tag != null && tag.equals(imagePath)) {
                    imageContainer.removeViewAt(i);
                    Log.d(TAG, "Image removed: " + imagePath);
                    return;
                }
            }
        }
        Log.e(TAG, "Image not found for deletion: " + imagePath);
    }

    private void saveImagePathToPreferences(String imagePath) {
        SharedPreferences sharedPreferences = getSharedPreferences("MyAppPrefs", MODE_PRIVATE);
        SharedPreferences.Editor editor = sharedPreferences.edit();
        Gson gson = new Gson();
        String imageUriListJson = sharedPreferences.getString("imageUriList", "[]");
        List<String> imageUriList = gson.fromJson(imageUriListJson, new TypeToken<List<String>>() {}.getType());
        if (imageUriList == null) {
            imageUriList = new ArrayList<>();
        }
        imageUriList.add(imagePath);
        String newImageUriListJson = gson.toJson(imageUriList);
        editor.putString("imageUriList", newImageUriListJson);
        editor.apply();
    }



    private void removeImagePathFromPreferences(String imagePath) {
        SharedPreferences sharedPreferences = getSharedPreferences("MyAppPrefs", MODE_PRIVATE);
        SharedPreferences.Editor editor = sharedPreferences.edit();
        String imageUriListJson = sharedPreferences.getString("imageUriList", "[]");
        Gson gson = new Gson();
        List<String> imageUriList = gson.fromJson(imageUriListJson, new TypeToken<List<String>>() {}.getType());
        imageUriList.remove(imagePath);
        String newImageUriListJson = gson.toJson(imageUriList);
        editor.putString("imageUriList", newImageUriListJson);
        editor.apply();
    }






    private void openCustomCamera() {
        Intent intent = new Intent(this, CameraActivity.class);
        cameraLauncher.launch(intent);
    }
}

//package com.example.camera_application;
//
//import android.Manifest;
//import android.content.ContentValues;
//import android.content.Intent;
//import android.content.pm.PackageManager;
//import android.graphics.Bitmap;
//import android.net.Uri;
//import android.os.Build;
//import android.os.Bundle;
//import android.os.Environment;
//import android.provider.MediaStore;
//import android.text.SpannableString;
//import android.text.Spanned;
//import android.text.style.ImageSpan;
//import android.util.Log;
//import android.widget.Button;
//import android.widget.EditText;
//import android.widget.ImageButton;
//import android.widget.ImageView;
//import android.widget.Toast;
//
//import androidx.activity.result.ActivityResultLauncher;
//import androidx.activity.result.contract.ActivityResultContracts;
//import androidx.annotation.NonNull;
//import androidx.annotation.Nullable;
//import androidx.appcompat.app.AppCompatActivity;
//import androidx.core.app.ActivityCompat;
//import androidx.core.content.ContextCompat;
//
//import java.io.File;
//import java.io.IOException;
//import java.io.OutputStream;
//
//public class MainActivity extends AppCompatActivity {
//    private ImageView imageView;
//    //private EditText editText;
//    private Bitmap capturedImage;
//
//    private final ActivityResultLauncher<Intent> cameraLauncher = registerForActivityResult(
//            new ActivityResultContracts.StartActivityForResult(),
//            result -> {
//                if (result.getResultCode() == RESULT_OK) {
//                    if (result.getData() != null && result.getData().getExtras() != null) {
//                        capturedImage = (Bitmap) result.getData().getExtras().get("data");
//                        imageView.setImageBitmap(capturedImage);
//                        //embedImageInEditText(capturedImage);
//                    }
//                }
//            }
//    );
//    private static final int REQUEST_WRITE_STORAGE = 112;
//    private static final int REQUEST_CAMERA_PERMISSION = 1;
//
//    @Override
//    protected void onCreate(Bundle savedInstanceState) {
//        super.onCreate(savedInstanceState);
//        setContentView(R.layout.activity_main);
//
//        imageView = findViewById(R.id.img_view);
//        //editText = findViewById(R.id.edit_text);
//        ImageButton btnCamera = findViewById(R.id.btn_camera);
//        //Button btnSave = findViewById(R.id.btn_save);
//
//        btnCamera.setOnClickListener(view -> openCamera());
//
////        btnSave.setOnClickListener(view -> {
////            if (capturedImage != null) {
////                if (ContextCompat.checkSelfPermission(this, Manifest.permission.WRITE_EXTERNAL_STORAGE)
////                        != PackageManager.PERMISSION_GRANTED) {
////                    // Permission is not granted, request it
////                    ActivityCompat.requestPermissions(this,
////                            new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE},
////                            REQUEST_WRITE_STORAGE);
////                } else {
////                    // Permission is granted, proceed with saving the image
////                    saveImageToMediaStore();
////                }
////            } else {
////                Toast.makeText(MainActivity.this, "Capture an image first", Toast.LENGTH_SHORT).show();
////            }
////        });
//
//    }
//
//    private void openCamera() {
//        if (ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA)
//                != PackageManager.PERMISSION_GRANTED) {
//            checkCameraPermission();
//        } else {
//            Intent cameraIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
//            if (cameraIntent.resolveActivity(getPackageManager()) != null) {
//                cameraLauncher.launch(cameraIntent);
//            }
//        }
//    }
//
//    private void checkCameraPermission() {
//        if (ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA)
//                != PackageManager.PERMISSION_GRANTED) {
//            ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.CAMERA},
//                    REQUEST_CAMERA_PERMISSION);
//        } else {
//            openCamera();
//        }
//    }
//
//    @Override
//    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
//        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
//        if (requestCode == REQUEST_WRITE_STORAGE) {
//            if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
//                saveImageToMediaStore();
//            } else {
//                Toast.makeText(this, "Write permission is required to save images", Toast.LENGTH_SHORT).show();
//            }
//        }
//    }
//
//
//
////    private void saveImageToMediaStore() {
////        if (capturedImage != null) {
////            ContentValues values = new ContentValues();
////            values.put(MediaStore.Images.Media.DISPLAY_NAME, "captured_image.jpg");
////            values.put(MediaStore.Images.Media.MIME_TYPE, "image/jpeg");
////            values.put(MediaStore.Images.Media.RELATIVE_PATH, Environment.DIRECTORY_PICTURES + "/MyApp"); // Scoped storage path
////
////            Uri uri = getContentResolver().insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, values);
////
////            if (uri != null) {
////                try (OutputStream outputStream = getContentResolver().openOutputStream(uri)) {
////                    if (outputStream != null) {
////                        capturedImage.compress(Bitmap.CompressFormat.JPEG, 100, outputStream);
////                        Toast.makeText(this, "Image saved", Toast.LENGTH_SHORT).show();
////                    } else {
////                        Toast.makeText(this, "Failed to get output stream", Toast.LENGTH_SHORT).show();
////                    }
////                } catch (IOException e) {
////                    e.printStackTrace();
////                    Toast.makeText(this, "Failed to save image: " + e.getMessage(), Toast.LENGTH_LONG).show();
////                }
////            } else {
////                Toast.makeText(this, "Failed to create image file URI", Toast.LENGTH_SHORT).show();
////            }
////        } else {
////            Toast.makeText(this, "No image to save", Toast.LENGTH_SHORT).show();
////        }
////    }
//private void saveImageToMediaStore() {
//    if (capturedImage != null) {
//        try {
//            // Define content values for the image
//            ContentValues values = new ContentValues();
//            values.put(MediaStore.Images.Media.DISPLAY_NAME, "captured_image.jpg");
//            values.put(MediaStore.Images.Media.MIME_TYPE, "image/jpeg");
//
//            // For API 29 and above, use RELATIVE_PATH to define the directory
//            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
//                values.put(MediaStore.Images.Media.RELATIVE_PATH, "Pictures/MyApp");
//            } else {
//                // For API below 29, use DATA to define the file path
//                File directory = getExternalFilesDir(Environment.DIRECTORY_PICTURES);
//                if (directory != null) {
//                    String filePath = new File(directory, "captured_image.jpg").getAbsolutePath();
//                    values.put(MediaStore.Images.Media.DATA, filePath);
//                } else {
//                    Toast.makeText(this, "Directory not found", Toast.LENGTH_SHORT).show();
//                    return;
//                }
//            }
//
//            // Insert the image into MediaStore
//            Uri uri = getContentResolver().insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, values);
//
//            if (uri != null) {
//                // Write the image data to the output stream
//                try (OutputStream outputStream = getContentResolver().openOutputStream(uri)) {
//                    if (outputStream != null) {
//                        capturedImage.compress(Bitmap.CompressFormat.JPEG, 100, outputStream);
//                        Toast.makeText(this, "Image saved", Toast.LENGTH_SHORT).show();
//                    } else {
//                        Toast.makeText(this, "Failed to open output stream", Toast.LENGTH_SHORT).show();
//                    }
//                } catch (Exception e) {
//                    e.printStackTrace();
//                    Toast.makeText(this, "Failed to save image", Toast.LENGTH_SHORT).show();
//                }
//            } else {
//                Toast.makeText(this, "Failed to create image file", Toast.LENGTH_SHORT).show();
//            }
//        } catch (Exception e) {
//            e.printStackTrace();
//            Toast.makeText(this, "Error occurred while saving image", Toast.LENGTH_SHORT).show();
//        }
//    } else {
//        Toast.makeText(this, "No image to save", Toast.LENGTH_SHORT).show();
//    }
//}
//
//
//
//
//
//
//
////    private void embedImageInEditText(Bitmap bitmap) {
////        Bitmap resizedBitmap = Bitmap.createScaledBitmap(bitmap, 100, 100, false);
////        SpannableString ss = new SpannableString(" ");
////        ImageSpan span = new ImageSpan(this, resizedBitmap);
////        ss.setSpan(span, 0, 1, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);
////        editText.getText().insert(editText.getSelectionStart(), ss);
////    }
//
//}

package com.example.camera_application;

import android.Manifest;
import android.content.ContentValues;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.provider.MediaStore;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.Toast;

import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import java.io.IOException;
import java.io.OutputStream;

public class MainActivity extends AppCompatActivity {
    private ImageView imageView;
    private Bitmap capturedImage;

    private final ActivityResultLauncher<Intent> cameraLauncher = registerForActivityResult(
            new ActivityResultContracts.StartActivityForResult(),
            result -> {
                if (result.getResultCode() == RESULT_OK) {
                    if (result.getData() != null && result.getData().getExtras() != null) {
                        capturedImage = (Bitmap) result.getData().getExtras().get("data");
                        imageView.setImageBitmap(capturedImage);
                    }
                }
            }
    );
    private static final int REQUEST_WRITE_STORAGE = 112;
    private static final int REQUEST_CAMERA_PERMISSION = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        imageView = findViewById(R.id.img_view);
        ImageButton btnCamera = findViewById(R.id.btn_camera);

        btnCamera.setOnClickListener(view -> openCamera());
    }

    private void openCamera() {
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA)
                != PackageManager.PERMISSION_GRANTED) {
            checkCameraPermission();
        } else {
            Intent cameraIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
            if (cameraIntent.resolveActivity(getPackageManager()) != null) {
                cameraLauncher.launch(cameraIntent);
            }
        }
    }

    private void checkCameraPermission() {
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA)
                != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.CAMERA},
                    REQUEST_CAMERA_PERMISSION);
        } else {
            openCamera();
        }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode == REQUEST_CAMERA_PERMISSION) {
            if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                openCamera();
            } else {
                Toast.makeText(this, "Camera permission is required", Toast.LENGTH_SHORT).show();
            }
        }
    }

    private void saveImageToMediaStore() {
        if (capturedImage != null) {
            try {
                ContentValues values = new ContentValues();
                values.put(MediaStore.Images.Media.DISPLAY_NAME, "captured_image.jpg");
                values.put(MediaStore.Images.Media.MIME_TYPE, "image/jpeg");

                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
                    values.put(MediaStore.Images.Media.RELATIVE_PATH, "Pictures/MyApp");
                } else {
                    String directory = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_PICTURES).toString();
                    String filePath = directory + "/captured_image.jpg";
                    values.put(MediaStore.Images.Media.DATA, filePath);
                }

                Uri uri = getContentResolver().insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, values);

                if (uri != null) {
                    try (OutputStream outputStream = getContentResolver().openOutputStream(uri)) {
                        if (outputStream != null) {
                            capturedImage.compress(Bitmap.CompressFormat.JPEG, 100, outputStream);
                            Toast.makeText(this, "Image saved", Toast.LENGTH_SHORT).show();
                        } else {
                            Toast.makeText(this, "Failed to open output stream", Toast.LENGTH_SHORT).show();
                        }
                    } catch (IOException e) {
                        e.printStackTrace();
                        Toast.makeText(this, "Failed to save image: " + e.getMessage(), Toast.LENGTH_LONG).show();
                    }
                } else {
                    Toast.makeText(this, "Failed to create image file URI", Toast.LENGTH_SHORT).show();
                }
            } catch (Exception e) {
                e.printStackTrace();
                Toast.makeText(this, "Error occurred while saving image", Toast.LENGTH_SHORT).show();
            }
        } else {
            Toast.makeText(this, "No image to save", Toast.LENGTH_SHORT).show();
        }
    }
}

























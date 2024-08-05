package com.example.project;

import android.content.Intent;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.util.Log;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;

import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

public class ImageDetailsActivity extends AppCompatActivity {

    private static final String TAG = "ImageDetailsActivity";
    private ImageView imageViewDetails;
    private TextView textFilePath;
    private TextView textFileType;
    private TextView textFileSize;
    private TextView textDateCaptured;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_image_details);

        imageViewDetails = findViewById(R.id.imageViewDetails);
        textFilePath = findViewById(R.id.textFilePath);
        textFileType = findViewById(R.id.textFileType);
        textFileSize = findViewById(R.id.textFileSize);
        textDateCaptured = findViewById(R.id.textDateCaptured);

        Intent intent = getIntent();
        String imageUriString = intent.getStringExtra("imageUri");

        Log.d(TAG, "Received image URI: " + imageUriString);

        if (imageUriString != null) {
            Uri imageUri = Uri.parse(imageUriString);

            Log.d(TAG, "Parsed image URI: " + imageUri);

            // Load the image into the ImageView using Glide
            Glide.with(this)
                    .load(imageUri)
                    .error(R.drawable.error_image) // Provide a placeholder in case of error
                    .into(imageViewDetails);

            File imageFile = new File(imageUri.getPath());
            Log.d(TAG, "Image file path: " + imageFile.getAbsolutePath());

            if (imageFile.exists()) {
                Log.d(TAG, "Image file exists.");
                textFilePath.setText("File Path: " + imageFile.getAbsolutePath());
                textFileType.setText("File Type: " + getFileExtension(imageFile));
                textFileSize.setText("File Size: " + (imageFile.length() / (1024 * 1024)) + " MB");
                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
                    textDateCaptured.setText("Date Captured: " + new SimpleDateFormat("yyyy-MM-dd HH:mm:ss", Locale.US).format(new Date(imageFile.lastModified())));
                }
            } else {
                Log.e(TAG, "File not found: " + imageFile.getAbsolutePath());
                Toast.makeText(this, "File not found", Toast.LENGTH_SHORT).show();
            }
        } else {
            Log.e(TAG, "No image URI received.");
        }
    }

    private String getFileExtension(File file) {
        String fileName = file.getName();
        int dotIndex = fileName.lastIndexOf('.');
        if (dotIndex > 0 && dotIndex < fileName.length() - 1) {
            return fileName.substring(dotIndex + 1);
        } else {
            return "unknown";
        }
    }
}

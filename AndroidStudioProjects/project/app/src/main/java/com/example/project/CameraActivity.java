package com.example.project;

import android.Manifest;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.Toast;

import androidx.camera.video.FileOutputOptions;
import androidx.camera.video.Recorder;
import androidx.camera.video.Recording;
import androidx.camera.video.VideoCapture;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.camera.core.AspectRatio;
import androidx.camera.core.CameraSelector;
import androidx.camera.core.ImageCapture;
import androidx.camera.core.ImageCaptureException;
import androidx.camera.core.Preview;
import androidx.camera.lifecycle.ProcessCameraProvider;
import androidx.camera.video.Quality;
import androidx.camera.video.QualitySelector;
import androidx.camera.video.Recorder;
import androidx.camera.video.VideoCapture;
import androidx.camera.video.VideoRecordEvent;
import androidx.camera.view.PreviewView;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import com.google.common.util.concurrent.ListenableFuture;
import com.theartofdev.edmodo.cropper.CropImage;
import com.theartofdev.edmodo.cropper.CropImageView;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.lang.reflect.Type;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class CameraActivity extends AppCompatActivity {

    private static final String TAG = "CameraActivity";
    private static final int REQUEST_CODE_PERMISSIONS = 10;
    private static final String[] REQUIRED_PERMISSIONS = new String[]{Manifest.permission.CAMERA, Manifest.permission.RECORD_AUDIO, Manifest.permission.WRITE_EXTERNAL_STORAGE, Manifest.permission.READ_EXTERNAL_STORAGE};

    private ImageCapture imageCapture;
    private ExecutorService cameraExecutor;
    private Button buttonCapture;
    private Button buttonImage;
    private Button buttonVideo;
    private Button buttonDocument;
    private View documentFrame;
    private ImageView croppedImageView;
    private String currentMode = "IMAGE"; // Default mode
    private VideoCapture<Recorder> videoCapture;
    private Recording recording;
    private boolean isRecording = false;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_camera);

        buttonCapture = findViewById(R.id.button_capture);
        buttonImage = findViewById(R.id.button_photo);
        buttonVideo = findViewById(R.id.button_video);
        buttonDocument = findViewById(R.id.button_document);
        documentFrame = findViewById(R.id.document_frame);
        croppedImageView = findViewById(R.id.cropped_image);
        cameraExecutor = Executors.newSingleThreadExecutor();

        if (allPermissionsGranted()) {
            startCamera();
        } else {
            ActivityCompat.requestPermissions(this, REQUIRED_PERMISSIONS, REQUEST_CODE_PERMISSIONS);
        }

        buttonCapture.setOnClickListener(v -> {
            if (currentMode.equals("IMAGE")) {
                takePhoto();
            }else if (currentMode.equals("VIDEO")) {
                if (isRecording) {
                    stopRecording();
                } else {
                    startRecording();
                }
            } else if (currentMode.equals("DOCUMENT")) {
                takeDocumentPhoto();
            }
        });

        buttonImage.setOnClickListener(v -> {
            currentMode = "IMAGE";
            buttonCapture.setText("Capture Image");
            documentFrame.setVisibility(View.GONE);
            croppedImageView.setVisibility(View.GONE);
            Log.d(TAG, "Mode changed to IMAGE");
            rebindCameraUseCases();
        });

        buttonDocument.setOnClickListener(v -> {
            currentMode = "DOCUMENT";
            buttonCapture.setText("Capture Document");
            documentFrame.setVisibility(View.VISIBLE);
            croppedImageView.setVisibility(View.GONE);
            Log.d(TAG, "Mode changed to DOCUMENT");
            rebindCameraUseCases();
        });

        buttonVideo.setOnClickListener(v -> {
            currentMode = "VIDEO";
            buttonCapture.setText("Start Recording");
            documentFrame.setVisibility(View.GONE);
            Log.d(TAG, "Mode changed to VIDEO");
            rebindCameraUseCases();
        });

    }

    private boolean allPermissionsGranted() {
        for (String permission : REQUIRED_PERMISSIONS) {
            if (ContextCompat.checkSelfPermission(this, permission) != PackageManager.PERMISSION_GRANTED) {
                Log.d(TAG, "Permission not granted: " + permission);
                return false;
            }
        }
        Log.d(TAG, "All permissions granted");
        return true;
    }

    private void startCamera() {
        ListenableFuture<ProcessCameraProvider> cameraProviderFuture = ProcessCameraProvider.getInstance(this);

        cameraProviderFuture.addListener(() -> {
            try {
                ProcessCameraProvider cameraProvider = cameraProviderFuture.get();
                Log.d(TAG, "Camera provider obtained");
                bindPreview(cameraProvider);
            } catch (ExecutionException | InterruptedException e) {
                Log.e(TAG, "Error getting camera provider", e);
            }
        }, ContextCompat.getMainExecutor(this));
    }

    private void bindPreview(ProcessCameraProvider cameraProvider) {
        PreviewView previewView = findViewById(R.id.preview_view);
        Preview.Builder previewBuilder = new Preview.Builder();

        // Adjust preview builder based on the current mode
        switch (currentMode) {
            case "IMAGE":
                previewBuilder.setTargetAspectRatio(AspectRatio.RATIO_4_3);
                break;
            case "DOCUMENT":
                previewBuilder.setTargetAspectRatio(AspectRatio.RATIO_16_9); // Adjust if needed
                break;
            case "VIDEO":
                previewBuilder.setTargetAspectRatio(AspectRatio.RATIO_16_9);
                break;
        }

        Preview preview = previewBuilder.build();

        if (currentMode.equals("IMAGE") || currentMode.equals("DOCUMENT")) {
            imageCapture = new ImageCapture.Builder()
                    .setTargetAspectRatio(currentMode.equals("IMAGE") ? AspectRatio.RATIO_4_3 : AspectRatio.RATIO_16_9)
                    .build();
        }else {
            videoCapture = VideoCapture.withOutput(new Recorder.Builder()
                    .setQualitySelector(QualitySelector.from(Quality.HD))
                    .build());
        }

        preview.setSurfaceProvider(previewView.getSurfaceProvider());

        CameraSelector cameraSelector = CameraSelector.DEFAULT_BACK_CAMERA;

        cameraProvider.unbindAll();

        if (currentMode.equals("IMAGE") || currentMode.equals("DOCUMENT")) {
            cameraProvider.bindToLifecycle(this, cameraSelector, preview, imageCapture);
        }else if (currentMode.equals("VIDEO")) {
            cameraProvider.bindToLifecycle(this, cameraSelector, preview, videoCapture);
        }

        Log.d(TAG, "Preview and use cases bound to lifecycle for mode: " + currentMode);
    }

    private void rebindCameraUseCases() {
        if (allPermissionsGranted()) {
            startCamera();
        } else {
            Toast.makeText(this, "Permissions not granted by the user.", Toast.LENGTH_SHORT).show();
        }
    }

    private void takePhoto() {
        if (imageCapture == null) {
            Log.e(TAG, "ImageCapture not initialized");
            Toast.makeText(this, "ImageCapture not initialized", Toast.LENGTH_SHORT).show();
            return;
        }

        File photoFile = new File(getExternalFilesDir(null),
                new SimpleDateFormat("yyyyMMddHHmmss", Locale.US).format(System.currentTimeMillis()) + ".jpg");

        ImageCapture.OutputFileOptions outputOptions = new ImageCapture.OutputFileOptions.Builder(photoFile).build();

        imageCapture.takePicture(outputOptions, ContextCompat.getMainExecutor(this), new ImageCapture.OnImageSavedCallback() {
            @Override
            public void onImageSaved(@NonNull ImageCapture.OutputFileResults outputFileResults) {
                Log.d(TAG, "Photo capture succeeded: " + photoFile.getAbsolutePath());
                Uri savedUri = Uri.fromFile(photoFile);
                Toast.makeText(CameraActivity.this, "Photo capture succeeded: " + savedUri, Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onError(@NonNull ImageCaptureException exception) {
                Log.e(TAG, "Photo capture failed: " + exception.getMessage(), exception);
                Toast.makeText(CameraActivity.this, "Photo capture failed: " + exception.getMessage(), Toast.LENGTH_SHORT).show();
            }
        });
    }
    private void startRecording() {
        if (videoCapture == null) {
            Log.e(TAG, "VideoCapture not initialized");
            Toast.makeText(this, "VideoCapture not initialized", Toast.LENGTH_SHORT).show();
            return;
        }

        File videoFile = new File(getExternalFilesDir(null),
                new SimpleDateFormat("yyyyMMddHHmmss", Locale.US).format(System.currentTimeMillis()) + ".mp4");

        FileOutputOptions outputOptions = new FileOutputOptions.Builder(videoFile).build();

        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.RECORD_AUDIO) != PackageManager.PERMISSION_GRANTED) {
            Log.e(TAG, "Audio recording permission not granted");
            return;
        }

        recording = videoCapture.getOutput().prepareRecording(this, outputOptions)
                .withAudioEnabled()
                .start(ContextCompat.getMainExecutor(this), videoRecordEvent -> {
                    if (videoRecordEvent instanceof VideoRecordEvent.Start) {
                        Log.d(TAG, "Video recording started");
                        buttonCapture.setText("Stop Recording");
                        isRecording = true;
                    } else if (videoRecordEvent instanceof VideoRecordEvent.Finalize) {
                        Log.d(TAG, "Video recording finalized");
                        buttonCapture.setText("Start Recording");
                        isRecording = false;
                        recording = null;
                    }
                });
    }

    private void stopRecording() {
        if (recording != null) {
            recording.stop();
            recording = null;
            Log.d(TAG, "Video recording stopped");
            Toast.makeText(this, "Video recording stopped", Toast.LENGTH_SHORT).show();
        }
    }

    private void takeDocumentPhoto() {
        if (imageCapture == null) {
            Log.e(TAG, "ImageCapture not initialized");
            Toast.makeText(this, "ImageCapture not initialized", Toast.LENGTH_SHORT).show();
            return;
        }

        File photoFile = new File(getExternalFilesDir(null),
                new SimpleDateFormat("yyyyMMddHHmmss", Locale.US).format(System.currentTimeMillis()) + "_document.jpg");

        ImageCapture.OutputFileOptions outputOptions = new ImageCapture.OutputFileOptions.Builder(photoFile).build();

        imageCapture.takePicture(outputOptions, ContextCompat.getMainExecutor(this), new ImageCapture.OnImageSavedCallback() {
            @Override
            public void onImageSaved(@NonNull ImageCapture.OutputFileResults outputFileResults) {
                Log.d(TAG, "Document photo capture succeeded: " + photoFile.getAbsolutePath());
                Toast.makeText(CameraActivity.this, "Document photo capture succeeded: " + photoFile.getAbsolutePath(), Toast.LENGTH_SHORT).show();

                // Save image path to SharedPreferences
                saveImagePath(photoFile.getAbsolutePath());

                // Launch CropImage activity for the captured document photo
                CropImage.activity(Uri.fromFile(photoFile))
                        .setGuidelines(CropImageView.Guidelines.ON)
                        .start(CameraActivity.this);
            }

            @Override
            public void onError(@NonNull ImageCaptureException exception) {
                Log.e(TAG, "Document photo capture failed", exception);
                Toast.makeText(CameraActivity.this, "Document photo capture failed", Toast.LENGTH_SHORT).show();
            }
        });
    }
    private void saveImagePath(String path) {
        SharedPreferences sharedPreferences = getSharedPreferences("ImagePaths", MODE_PRIVATE);
        SharedPreferences.Editor editor = sharedPreferences.edit();

        // Get the current list of paths
        Gson gson = new Gson();
        String json = sharedPreferences.getString("paths", null);
        List<String> paths;
        if (json == null) {
            paths = new ArrayList<>();
        } else {
            Type type = new TypeToken<List<String>>() {}.getType();
            paths = gson.fromJson(json, type);
        }

        // Add the new path and save the list back to SharedPreferences
        paths.add(0, path); // Add to the beginning of the list to show newest first
        json = gson.toJson(paths);
        editor.putString("paths", json);
        editor.apply();
    }


    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == CropImage.CROP_IMAGE_ACTIVITY_REQUEST_CODE) {
            CropImage.ActivityResult result = CropImage.getActivityResult(data);
            if (resultCode == RESULT_OK) {
                Uri resultUri = result.getUri();

                // Get existing list of image URIs from shared preferences
                SharedPreferences sharedPreferences = getSharedPreferences("MyAppPrefs", MODE_PRIVATE);
                SharedPreferences.Editor editor = sharedPreferences.edit();
                String imageUriListJson = sharedPreferences.getString("imageUriList", "[]");
                Gson gson = new Gson();
                List<String> imageUriList = gson.fromJson(imageUriListJson, new TypeToken<List<String>>() {}.getType());

                // Add new image URI to the list and save it back to shared preferences
                imageUriList.add(0, resultUri.toString()); // Add to the beginning of the list
                editor.putString("imageUriList", gson.toJson(imageUriList));
                editor.apply();

                // Launch MainActivity with the updated image list
                Intent intent = new Intent(CameraActivity.this, MainActivity.class);
                startActivity(intent);
            } else if (resultCode == CropImage.CROP_IMAGE_ACTIVITY_RESULT_ERROR_CODE) {
                Exception error = result.getError();
                Log.e(TAG, "Crop error", error);
                Toast.makeText(this, "Crop error: " + error.getMessage(), Toast.LENGTH_SHORT).show();
            }
        }
    }




    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode == REQUEST_CODE_PERMISSIONS) {
            if (allPermissionsGranted()) {
                startCamera();
            } else {
                Toast.makeText(this, "Permissions not granted by the user.", Toast.LENGTH_SHORT).show();
                finish();
            }
        }
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        cameraExecutor.shutdown();
    }
}

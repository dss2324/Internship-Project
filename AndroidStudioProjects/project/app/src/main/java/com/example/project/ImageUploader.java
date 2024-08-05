package com.example.project;

import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;
import java.io.File;
import java.io.IOException;

public class ImageUploader {

    private static final MediaType MEDIA_TYPE_IMAGE = MediaType.parse("image/jpeg"); // Adjust MIME type if needed
    private static final String UPLOAD_URL = "http://example.com/upload_image.php"; // Replace with actual URL

    // Method to upload an image
    public static void uploadImage(String filePath, String description, UploadCallback callback) {
        OkHttpClient client = new OkHttpClient();

        // Prepare the file
        File file = new File(filePath);
        RequestBody fileBody = RequestBody.create(file, MEDIA_TYPE_IMAGE);

        // Create the multipart request body
        RequestBody requestBody = new MultipartBody.Builder()
                .setType(MultipartBody.FORM)
                .addFormDataPart("file", file.getName(), fileBody)
                .addFormDataPart("description", description) // Add description if needed
                .build();

        // Create the request
        Request request = new Request.Builder()
                .url(UPLOAD_URL)
                .post(requestBody)
                .build();

        // Execute the request
        client.newCall(request).enqueue(new okhttp3.Callback() {
            @Override
            public void onFailure(okhttp3.Call call, IOException e) {
                // Handle the error
                if (callback != null) {
                    callback.onUploadFailed(e.getMessage());
                }
            }

            @Override
            public void onResponse(okhttp3.Call call, Response response) throws IOException {
                if (response.isSuccessful()) {
                    // Handle the response
                    String responseData = response.body().string();
                    if (callback != null) {
                        callback.onUploadSuccess(responseData);
                    }
                } else {
                    if (callback != null) {
                        callback.onUploadFailed("Upload failed: " + response.message());
                    }
                }
            }
        });
    }

    // Callback interface for upload results
    public interface UploadCallback {
        void onUploadSuccess(String response);
        void onUploadFailed(String errorMessage);
    }
}

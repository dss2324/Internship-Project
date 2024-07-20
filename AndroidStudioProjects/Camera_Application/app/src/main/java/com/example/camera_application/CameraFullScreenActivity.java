//package com.example.camera_application;
//
//import android.content.Intent;
//import android.graphics.Bitmap;
//import android.graphics.BitmapFactory;
//import android.hardware.Camera;
//import android.os.Bundle;
//import android.view.SurfaceHolder;
//import android.view.SurfaceView;
//import android.view.View;
//import android.widget.Button;
//import android.widget.FrameLayout;
//
//import androidx.appcompat.app.AppCompatActivity;
//
//import java.io.IOException;
//
//public class CameraFullScreenActivity extends AppCompatActivity {
//    private Camera camera;
//    private SurfaceView surfaceView;
//    private SurfaceHolder surfaceHolder;
//
//    @Override
//    protected void onCreate(Bundle savedInstanceState) {
//        super.onCreate(savedInstanceState);
//        setContentView(R.layout.activity_camera_fullscreen);
//
//        camera = getCameraInstance();
//        surfaceView = new SurfaceView(this);
//        surfaceHolder = surfaceView.getHolder();
//
//        FrameLayout frameLayout = findViewById(R.id.camera_frame);
//        frameLayout.addView(surfaceView);
//
//        surfaceHolder.addCallback(new SurfaceHolder.Callback() {
//            @Override
//            public void surfaceCreated(SurfaceHolder holder) {
//                try {
//                    camera.setPreviewDisplay(holder);
//                    camera.startPreview();
//                } catch (IOException e) {
//                    e.printStackTrace();
//                }
//            }
//
//            @Override
//            public void surfaceChanged(SurfaceHolder holder, int format, int width, int height) {
//                if (surfaceHolder.getSurface() == null) {
//                    return;
//                }
//
//                try {
//                    camera.stopPreview();
//                } catch (Exception e) {
//                    e.printStackTrace();
//                }
//
//                try {
//                    camera.setPreviewDisplay(surfaceHolder);
//                    camera.startPreview();
//                } catch (IOException e) {
//                    e.printStackTrace();
//                }
//            }
//
//            @Override
//            public void surfaceDestroyed(SurfaceHolder holder) {
//                if (camera != null) {
//                    camera.stopPreview();
//                    camera.release();
//                    camera = null;
//                }
//            }
//        });
//
//        Button captureButton = findViewById(R.id.btn_capture);
//        captureButton.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                camera.takePicture(null, null, new Camera.PictureCallback() {
//                    @Override
//                    public void onPictureTaken(byte[] data, Camera camera) {
//                        Bitmap bitmap = BitmapFactory.decodeByteArray(data, 0, data.length);
//                        Intent resultIntent = new Intent();
//                        resultIntent.putExtra("image", bitmap);
//                        setResult(RESULT_OK, resultIntent);
//                        finish();
//                    }
//                });
//            }
//        });
//    }
//
//    private Camera getCameraInstance() {
//        Camera camera = null;
//        try {
//            camera = Camera.open();
//        } catch (Exception e) {
//            e.printStackTrace();
//        }
//        return camera;
//    }
//}


package com.example.camera_application;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.hardware.Camera;
import android.os.Bundle;
import android.view.SurfaceHolder;
import android.view.SurfaceView;
import android.widget.Button;
import android.widget.FrameLayout;

import androidx.appcompat.app.AppCompatActivity;

import java.io.IOException;

public class CameraFullScreenActivity extends AppCompatActivity {
    private Camera camera;
    private SurfaceView surfaceView;
    private SurfaceHolder surfaceHolder;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_camera_fullscreen);

        camera = getCameraInstance();
        surfaceView = findViewById(R.id.camera_preview);
        surfaceHolder = surfaceView.getHolder();

        surfaceHolder.addCallback(new SurfaceHolder.Callback() {
            @Override
            public void surfaceCreated(SurfaceHolder holder) {
                try {
                    camera.setPreviewDisplay(holder);
                    camera.startPreview();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }

            @Override
            public void surfaceChanged(SurfaceHolder holder, int format, int width, int height) {
                if (surfaceHolder.getSurface() == null) {
                    return;
                }

                try {
                    camera.stopPreview();
                } catch (Exception e) {
                    // ignore
                }

                try {
                    camera.setPreviewDisplay(surfaceHolder);
                    camera.startPreview();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }

            @Override
            public void surfaceDestroyed(SurfaceHolder holder) {
                // release camera preview
            }
        });

        Button captureButton = findViewById(R.id.btn_capture);
        captureButton.setOnClickListener(v -> {
            camera.takePicture(null, null, (data, cam) -> {
                Bitmap bitmap = BitmapFactory.decodeByteArray(data, 0, data.length);
                Intent intent = new Intent(CameraFullScreenActivity.this, MainActivity.class);
                intent.putExtra("capturedImage", bitmap);
                setResult(RESULT_OK, intent);
                finish();
            });
        });
    }

    private Camera getCameraInstance() {
        Camera c = null;
        try {
            c = Camera.open();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return c;
    }

    @Override
    protected void onPause() {
        super.onPause();
        if (camera != null) {
            camera.release();
            camera = null;
        }
    }
}

package com.example.intentwsplayer;

import android.content.Context;
import android.util.Log;
import android.webkit.WebResourceRequest;
import android.webkit.WebView;
import android.webkit.WebViewClient;

import java.util.Locale;

class MyWebViewClient extends WebViewClient {

  private static final String TAG = MyWebViewClient.class.getName();

  private Context mContext;
  private JsInterface mJsInterface;

  public MyWebViewClient(Context context, JsInterface jsInterface) {
    mContext = context;
    mJsInterface = jsInterface;
  }

  @Override
  public void onPageFinished(WebView view, String url) {
    super.onPageFinished(view, url);
//    view.loadUrl("javascript:window.jsinterface.readhtml(document.body.innerHTML);");
//    Log.d(TAG, String.format("WebViewClient html : %s", mJsInterface.mHtmlSource));
  }

  @Override
  public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
    String url = String.valueOf(request.getUrl());
    String method = request.getMethod();
    Log.d(TAG, String.format(Locale.getDefault(), "WebViewClient LinkURL: %s", url));
    Log.d(TAG, String.format(Locale.getDefault(), "WebViewClient Method: %s", method));
    return false;
  }


}

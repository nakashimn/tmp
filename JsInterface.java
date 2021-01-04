package com.example.intentwsplayer;

import android.webkit.JavascriptInterface;

class JsInterface {

  public String mHtmlSource = "";

  @JavascriptInterface
  public void readhtml(String html){
    mHtmlSource = html;
  }
}

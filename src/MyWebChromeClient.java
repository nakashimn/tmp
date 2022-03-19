package com.example.intentwsplayer;

import android.util.Log;
import android.webkit.WebChromeClient;
import android.webkit.WebView;

class MyWebChromeClient extends WebChromeClient {

  private final String TAG = MyWebChromeClient.class.getName();

  private final int mSleepMilliSec = 10;
  private final String mIdAnchor = "<li class=\"nav-item mt-1\">";
  private final String[] mIdRegex = {"<li class=\"nav-item mt-1\"><i class=\"fas fa-user-circle \"></i>", "</li>"};
  private final String mContentsUrlAnchor = "http://cdn-dl6.webstream.ne.jp/wns/";
  private final String[] mContentsUrlRegex = {"<source src=\"", "\" type=\"video/mp4\">"};

  private JsInterface mJsInterface = null;

  private String mUrl = "";
  private String mUserId = "";
  private String mContentsUrl = "";
  private Boolean mPlayingMovie = false;

  public MyWebChromeClient(JsInterface jsInterface) {
    super();
    Log.d(TAG, "MyWebChromeClient is called.");
    mJsInterface = jsInterface;
  }

  @Override
  public void onProgressChanged(WebView view, int newProgress) {
    Log.d(TAG, "onProgressChanged is called.");
    super.onProgressChanged(view, newProgress);
    if(newProgress == 100){
      try {
        Thread.sleep(mSleepMilliSec);
        readUserInfo(view);
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
    }
  }

  private Boolean readUserInfo(WebView view){

    mUrl = view.getUrl();
    String html = fetchHtmlSource(view);
    if(html.contains(mIdAnchor)){
      mUserId = readUserId(html);
    }
    if(html.contains(mContentsUrlAnchor)){
      mContentsUrl = readContentsUrl(html);
      mPlayingMovie = true;
    } else {
      mContentsUrl = "";
      mPlayingMovie = false;
    }

//    Log.d(TAG, String.format("WebChromeClient html : %s", html));
    Log.d(TAG, String.format("WebChromeClient url : %s", mUrl));
    Log.d(TAG, String.format("WebChromeClient UserId : %s", mUserId));
    Log.d(TAG, String.format("WebChromeClient ContentsUrl : %s", mContentsUrl));
    Log.d(TAG, String.format("WebChromeClient PlayingMovie : %b", mPlayingMovie));
    return true;
  }

  private String fetchHtmlSource(WebView view){
    view.loadUrl("javascript:window.jsinterface.readhtml(document.body.innerHTML);");
    return mJsInterface.mHtmlSource;
  }

  private String readUserId(String html){
    return (html.split(mIdRegex[0])[1]).split(mIdRegex[1])[0];
  }

  private String readContentsUrl(String html){
    return (html.split(mContentsUrlRegex[0])[1].split(mContentsUrlRegex[1])[0]);
  }

  public String getUserId(){
    return mUserId;
  }

  public String getContentsUrl(){
    return mContentsUrl;
  }

  public Boolean getPlayingMovieFlag(){
    return mPlayingMovie;
  }

}

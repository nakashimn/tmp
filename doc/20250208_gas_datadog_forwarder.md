## 挨拶

## 背景

## 作ったもの

https://github.com/nakashimn/gas-datadog-logger


## 使い方


// 1. DatadogAPIKeyを取得 (※スクリプトプロパティでの定義を推奨)
const scriptProperties = PropertiesService.getScriptProperties();
const ddApiKey = scriptProperties.getProperty('DD-API-KEY');

// 2. ScriptId, ScriptNameを取得
const scriptId = ScriptApp.getScriptId();
const scriptName = DriveApp.getFileById(scriptId).getName();

// 3. DatadogAPIKey, ScriptId, ScriptName, tagを引数にDatadogLoggerをインスタンス化
const ddLogger = createDatadogLogger(ddApiKey, scriptId, scriptName, tags={'version': '1.0.0'});

// [Example]

// level:DEBUG のログを送付する
ddLogger.debug('debug message.');

// Contentに status:SUCCESSを追加し level:WARNING のログを送付する
ddLogger.warn('warning message.', extra={'status': 'SUCCESS'});



## 最後に

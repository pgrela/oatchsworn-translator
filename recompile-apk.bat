set apkdir=j:\downloads\Oathsworn-ItD-v1-4_decompile_xml
set language=pl
echo We're working with %language%
xcopy output-%language%\raw\*.mp3 %apkdir%\resources\package_1\res\raw /y /d
xcopy output-%language%\strings.xml %apkdir%\resources\package_1\res\values /y /d
del %apkdir%_out.apk
%userprofile%\.jdks\azul-21.0.1\bin\java.exe -jar %userprofile%\apps\APKEditor-1.3.8.jar b -i %apkdir%
%userprofile%\AppData\Local\Android\Sdk\build-tools\35.0.0-rc4\apksigner.bat sign --ks-key-alias alias_name --ks %userprofile%\my-release-key.keystore --ks-pass pass:f7R14dZFsG443LmW0l --key-pass pass:f7R14dZFsG443LmW0l j:\downloads\Oathsworn-ItD-v1-4_decompile_xml_out.apk
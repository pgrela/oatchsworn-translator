set apkfile=j:\downloads\Oathsworn-ItD-v1-4.apk
set apkdir=j:\downloads\Oathsworn-ItD-v1-4_decompile_xml

rmdir %apkdir% /s
%userprofile%\.jdks\azul-21.0.1\bin\java.exe -jar %userprofile%\apps\APKEditor-1.3.8.jar d -i %apkfile%
xcopy %apkdir%\resources\package_1\res\values\strings.xml input\strings.xml /y /d
xcopy %apkdir%\path-map.json input\path-map.json /y /d
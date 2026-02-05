Android Watchface Build Pipeline
Purpose
Build AAB/APK from watchface assets using Gradle.
Build Script
Location: /opt/factory/bin/build_wff_aab.sh
Build Steps
Copy assets to project: /opt/factory/samples/wear-os-samples/
Update build.gradle with version/name
Run: ./gradlew bundleRelease
Output: app/build/outputs/bundle/release/app-release.aab
Testing
# Install on emulator/device
adb install -r app-release.aab

# Screenshot
adb shell screencap -p /sdcard/test.png
adb pull /sdcard/test.png
Common Issues
Gradle daemon: Kill with ./gradlew --stop
SDK not found: Check ANDROID_HOME env var
Build failure: Check build/ logs
Evidence
Save build logs + AAB to evidence directory.

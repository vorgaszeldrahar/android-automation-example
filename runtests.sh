#!/usr/bin/env bash
set -e

# Start Appium if it's not already running
APPIUM=$(ps -ef | grep "appium/build/lib/main.js" | head -1 | grep -v "grep" | cut -d " " -f 4)
if [ "${APPIUM}" = '' ]; then
  # Launch Appium using the same command as the App
  echo "Starting Appium"
  '/Applications/Appium.app/Contents/Resources/node/bin/node' /Applications/Appium.app/Contents/Resources/node_modules/appium/build/lib/main.js --address "127.0.0.1" --session-override --debug-log-spacing --platform-version "8.1" --platform-name "iOS" --show-ios-log --default-device &
else
  echo "Appium is already running under pid $APPIUM"
fi

# Start the Android emulator/simulator device if it is not already running
EMULATOR_PID=$(ps -ef | grep qemu-system-i386 | head -1 | grep -v "grep" | cut -d " " -f4)
if [ "${EMULATOR_PID}" = '' ]; then
  emulator -avd Nexus_5X_API_23 &
  adb -e wait-for-device
else
  echo "Emulator is already running under pid $EMULATOR_PID"
fi

# Remove the old virtualenv
rm -rf ./env/

# Create a fresh one
virtualenv -p python3.4 env

# activate the virtualenv
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the tests
python main.py


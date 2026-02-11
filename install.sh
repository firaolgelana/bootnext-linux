#!/bin/bash

# Define where to install
INSTALL_DIR="/opt/quickboot"
BIN_DIR="/usr/local/bin"

echo "🚀 Installing QuickBoot..."

# 1. Create directory
sudo mkdir -p $INSTALL_DIR

# 2. Copy files (excluding tests and cache)
echo "📂 Copying files..."
sudo cp -r core ui main.py config.py requirements.txt $INSTALL_DIR/

# 3. Create a startup script
echo "🔗 Creating command..."
# This little script runs python inside the install folder
cat <<EOF | sudo tee $BIN_DIR/quickboot
#!/bin/bash
cd $INSTALL_DIR
sudo python3 main.py "\$@"
EOF

# 4. Make it executable
sudo chmod +x $BIN_DIR/quickboot

echo "✅ Success! You can now run 'quickboot' from anywhere."
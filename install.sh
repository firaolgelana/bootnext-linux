#!/bin/bash

INSTALL_DIR="/opt/quickboot"
BIN_DIR="/usr/local/bin"
REPO_URL="https://github.com/firaolgelana/bootnext-linux.git"

echo "🚀 Installing QuickBoot..."

# Check Python
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 is required."
    exit 1
fi

# Check git
if ! command -v git &> /dev/null
then
    echo "❌ Git is required."
    exit 1
fi

# Check efibootmgr (very important for your tool)
if ! command -v efibootmgr &> /dev/null
then
    echo "❌ efibootmgr is required."
    echo "Install it with: sudo apt install efibootmgr"
    exit 1
fi

# Remove old installation
sudo rm -rf $INSTALL_DIR

# Clone repository
echo "📥 Cloning repository..."
sudo git clone $REPO_URL $INSTALL_DIR

# Create launcher command
echo "🔗 Creating command..."
sudo tee $BIN_DIR/quickboot > /dev/null <<EOF
#!/bin/bash
python3 $INSTALL_DIR/main.py "\$@"
EOF

# Make executable
sudo chmod +x $BIN_DIR/quickboot

echo "✅ Installation complete!"
echo "👉 Run with: sudo quickboot windows"

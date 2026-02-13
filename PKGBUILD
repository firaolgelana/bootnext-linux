# Maintainer: Firaol Gelana
pkgname=quickboot
pkgver=1.0.0
pkgrel=1
pkgdesc="Reboot directly into Windows from Linux one time."
arch=('any')
url="https://github.com/firaolgelana/bootnext-linux"
license=('MIT')
depends=('python' 'efibootmgr')
source=("git+$url.git#tag=v$pkgver")
sha256sums=('SKIP')

package() {
    mkdir -p "$pkgdir/opt/quickboot"
    mkdir -p "$pkgdir/usr/bin"
    
    # Copy files
    cp -r "$srcdir/quickboot"/* "$pkgdir/opt/quickboot/"
    
    # Create launcher
    echo "#!/bin/bash" > "$pkgdir/usr/bin/quickboot"
    echo 'if [ "$EUID" -ne 0 ]; then echo "Root required"; exit 1; fi' >> "$pkgdir/usr/bin/quickboot"
    echo "python /opt/quickboot/main.py \"\$@\"" >> "$pkgdir/usr/bin/quickboot"
    
    chmod +x "$pkgdir/usr/bin/quickboot"
}

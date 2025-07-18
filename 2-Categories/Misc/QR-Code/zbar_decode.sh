#!/bin/bash
# Decode QR code image using zbarimg

if [ -z "$1" ]; then
    echo "Usage: $0 <qr-image-file>"
    exit 1
fi

zbarimg "$1" | cut -d ":" -f2-
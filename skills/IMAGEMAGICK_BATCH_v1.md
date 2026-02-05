ImageMagick Asset Pipeline
Purpose
Batch process watchface PNGs: resize, mask, optimize.
Scripts
/opt/factory/bin/viewer/render_round.sh - Round mask for preview
/opt/factory/bin/viewer/render_watchface.sh - Generic processing
Common Operations
# Resize to 454x454
convert input.png -resize 454x454! output.png

# Apply round mask
convert input.png -resize 454x454! \
  \( -size 454x454 xc:black -fill white -draw "circle 227,227 227,0" -alpha copy \) \
  -compose DstIn -composite output.png

# Batch process directory
for f in /path/*.png; do
  convert "$f" -resize 454x454! "/output/$(basename $f)"
done

# Optimize size
pngquant --quality 80-95 input.png -o output.png
Quality Checks
File size: <100KB for preview
Dimensions: exactly 454x454
Transparency: preserved for round mask
Evidence
Save before/after screenshots in evidence directory.

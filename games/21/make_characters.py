from PIL import Image, ImageDraw, ImageFilter, ImageFont
import math

# We create 650x700 high-res illustration portraits matching guard_char.png style

def create_doctor_portrait():
    w, h = 650, 700
    im = Image.new('RGBA', (w, h), (18, 22, 32, 255))
    draw = ImageDraw.Draw(im)

    # 1. Background Palace Interior Glow
    for y in range(h):
        ratio = y / h
        r = int(14 + ratio * 16)
        g = int(18 + ratio * 16)
        b = int(28 + ratio * 20)
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255))

    # Ambient warm lantern light behind
    glow = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    gdraw.ellipse([w*0.5 - 180, h*0.2 - 100, w*0.5 + 180, h*0.2 + 260], fill=(230, 110, 60, 50))
    glow = glow.filter(ImageFilter.GaussianBlur(40))
    im = Image.alpha_composite(im, glow)
    draw = ImageDraw.Draw(im)

    # 2. Dark Blue Silk Hanbok Robe (도포)
    robe_pts = [
        (w*0.08, h), (w*0.18, h*0.58), (w*0.35, h*0.48), 
        (w*0.5, h*0.58), (w*0.65, h*0.48), (w*0.82, h*0.58), (w*0.92, h)
    ]
    draw.polygon(robe_pts, fill=(28, 48, 76, 255))
    draw.polygon([(w*0.32, h), (w*0.42, h*0.55), (w*0.5, h*0.68), (w*0.58, h*0.55), (w*0.68, h)], fill=(22, 38, 62, 255))

    # White Collar (동정깃)
    draw.polygon([(w*0.42, h*0.48), (w*0.5, h*0.62), (w*0.46, h*0.62), (w*0.38, h*0.48)], fill=(245, 240, 230, 255))
    draw.polygon([(w*0.58, h*0.48), (w*0.5, h*0.62), (w*0.54, h*0.62), (w*0.62, h*0.48)], fill=(240, 235, 225, 255))
    draw.polygon([(w*0.48, h*0.50), (w*0.5, h*0.54), (w*0.52, h*0.50)], fill=(150, 40, 40, 255))

    # Amber Bead & Jade Medallion
    draw.line([(w*0.5, h*0.62), (w*0.5, h*0.9)], fill=(215, 160, 60, 255), width=5)
    draw.ellipse([w*0.5 - 18, h*0.8 - 18, w*0.5 + 18, h*0.8 + 18], fill=(60, 140, 105, 255), outline=(215, 160, 60, 255), width=3)

    # 3. Neck & Handsome Intellectual Face
    neck_pts = [(w*0.44, h*0.42), (w*0.44, h*0.52), (w*0.56, h*0.52), (w*0.56, h*0.42)]
    draw.polygon(neck_pts, fill=(242, 202, 178, 255))

    # Face Oval with handsome jawline
    face_pts = [
        (w*0.36, h*0.30), (w*0.36, h*0.40), (w*0.42, h*0.48), 
        (w*0.50, h*0.51), (w*0.58, h*0.48), (w*0.64, h*0.40), (w*0.64, h*0.30)
    ]
    draw.polygon(face_pts, fill=(252, 222, 202, 255))

    # Shading on jaw & neck
    jaw_shade = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    js_draw = ImageDraw.Draw(jaw_shade)
    js_draw.polygon([(w*0.40, h*0.46), (w*0.5, h*0.52), (w*0.60, h*0.46), (w*0.5, h*0.55)], fill=(180, 120, 95, 80))
    jaw_shade = jaw_shade.filter(ImageFilter.GaussianBlur(6))
    im = Image.alpha_composite(im, jaw_shade)
    draw = ImageDraw.Draw(im)

    # Soft Blush & Manga Eyes
    draw.ellipse([w*0.38, h*0.38, w*0.44, h*0.42], fill=(240, 130, 130, 90))
    draw.ellipse([w*0.56, h*0.38, w*0.62, h*0.42], fill=(240, 130, 130, 90))

    # Intellectual Sharp Eyes
    # Left Eye
    draw.polygon([(w*0.40, h*0.34), (w*0.44, h*0.33), (w*0.47, h*0.35), (w*0.43, h*0.36)], fill=(25, 25, 30, 255))
    draw.ellipse([w*0.42, h*0.335, w*0.44, h*0.355], fill=(255, 255, 255, 255))
    # Right Eye
    draw.polygon([(w*0.53, h*0.35), (w*0.56, h*0.33), (w*0.60, h*0.34), (w*0.57, h*0.36)], fill=(25, 25, 30, 255))
    draw.ellipse([w*0.56, h*0.335, w*0.58, h*0.355], fill=(255, 255, 255, 255))

    # Eyebrows
    draw.line([(w*0.38, h*0.31), (w*0.46, h*0.29)], fill=(40, 30, 25, 255), width=4)
    draw.line([(w*0.54, h*0.29), (w*0.62, h*0.31)], fill=(40, 30, 25, 255), width=4)

    # Nose & Calm Lips
    draw.line([(w*0.50, h*0.35), (w*0.49, h*0.41), (w*0.51, h*0.41)], fill=(190, 135, 110, 255), width=2)
    draw.line([(w*0.47, h*0.445), (w*0.53, h*0.445)], fill=(160, 75, 70, 255), width=3)

    # 4. Korean Gat Hat (갓)
    # Gat Strings (갓끈 - Amber & Jade beads hanging down gracefully)
    draw.line([(w*0.35, h*0.24), (w*0.32, h*0.55)], fill=(225, 170, 50, 255), width=4)
    draw.line([(w*0.65, h*0.24), (w*0.68, h*0.55)], fill=(225, 170, 50, 255), width=4)
    draw.ellipse([w*0.31, h*0.42, w*0.33, h*0.45], fill=(60, 150, 110, 255))
    draw.ellipse([w*0.67, h*0.42, w*0.69, h*0.45], fill=(60, 150, 110, 255))

    # Gat Crown (모정 - Cylindrical black horsehair hat)
    draw.polygon([(w*0.38, h*0.22), (w*0.41, h*0.07), (w*0.59, h*0.07), (w*0.62, h*0.22)], fill=(24, 25, 30, 255))
    draw.ellipse([w*0.41, h*0.06, w*0.59, h*0.08], fill=(35, 36, 42, 255))
    # Gat Brim (양태 - Wide black brim)
    draw.ellipse([w*0.16, h*0.19, w*0.84, h*0.27], fill=(22, 24, 28, 255), outline=(50, 52, 60, 255), width=3)

    # Smooth subtle comic lineart finish
    im = im.convert('RGB')
    im.save('doctor_char.png')
    print('doctor_char.png created successfully!')

def create_court_lady_portrait():
    w, h = 650, 700
    im = Image.new('RGBA', (w, h), (18, 22, 32, 255))
    draw = ImageDraw.Draw(im)

    # Background Palace Interior Glow
    for y in range(h):
        ratio = y / h
        r = int(14 + ratio * 18)
        g = int(16 + ratio * 14)
        b = int(24 + ratio * 20)
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255))

    # Ambient soft pink/magenta glow
    glow = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    gdraw.ellipse([w*0.5 - 180, h*0.2 - 100, w*0.5 + 180, h*0.2 + 260], fill=(220, 70, 110, 45))
    glow = glow.filter(ImageFilter.GaussianBlur(40))
    im = Image.alpha_composite(im, glow)
    draw = ImageDraw.Draw(im)

    # 1. Gache Hair (Large traditional wig)
    draw.ellipse([w*0.26, h*0.16, w*0.74, h*0.42], fill=(24, 22, 28, 255))
    draw.ellipse([w*0.38, h*0.11, w*0.62, h*0.23], fill=(135, 35, 65, 255), outline=(215, 160, 60, 255), width=3)
    # Golden Jade Hairpin (비녀)
    draw.line([(w*0.18, h*0.18), (w*0.82, h*0.18)], fill=(220, 175, 60, 255), width=8)
    draw.ellipse([w*0.81, h*0.17, w*0.84, h*0.19], fill=(60, 160, 120, 255))

    # 2. Emerald Green & Crimson Royal Dangui (당의)
    draw.polygon([(w*0.08, h), (w*0.22, h*0.62), (w*0.38, h*0.52), (w*0.5, h*0.60), (w*0.62, h*0.52), (w*0.78, h*0.62), (w*0.92, h)], fill=(28, 65, 52, 255))
    # Crimson inner bodice
    draw.polygon([(w*0.30, h), (w*0.40, h*0.54), (w*0.5, h*0.66), (w*0.60, h*0.54), (w*0.70, h)], fill=(145, 42, 65, 255))

    # White Collar (동정깃) & Ribbon
    draw.polygon([(w*0.42, h*0.50), (w*0.5, h*0.64), (w*0.46, h*0.64), (w*0.38, h*0.50)], fill=(250, 248, 244, 255))
    draw.polygon([(w*0.58, h*0.50), (w*0.5, h*0.64), (w*0.54, h*0.64), (w*0.62, h*0.50)], fill=(245, 242, 238, 255))
    # Purple Ribbon (고름)
    draw.polygon([(w*0.49, h*0.64), (w*0.47, h*0.92), (w*0.52, h*0.92), (w*0.53, h*0.64)], fill=(85, 25, 45, 255))

    # 3. Graceful Face & Features
    face_pts = [
        (w*0.38, h*0.32), (w*0.38, h*0.42), (w*0.44, h*0.49), 
        (w*0.50, h*0.52), (w*0.56, h*0.49), (w*0.62, h*0.42), (w*0.62, h*0.32)
    ]
    draw.polygon(face_pts, fill=(255, 230, 215, 255))

    # Soft Cheek Blush
    draw.ellipse([w*0.39, h*0.40, w*0.45, h*0.44], fill=(245, 120, 140, 100))
    draw.ellipse([w*0.55, h*0.40, w*0.61, h*0.44], fill=(245, 120, 140, 100))

    # Elegant Cat Eyes
    # Left Eye
    draw.polygon([(w*0.41, h*0.36), (w*0.45, h*0.35), (w*0.48, h*0.37), (w*0.44, h*0.38)], fill=(30, 25, 30, 255))
    draw.ellipse([w*0.43, h*0.355, w*0.45, h*0.375], fill=(255, 255, 255, 255))
    # Right Eye
    draw.polygon([(w*0.52, h*0.37), (w*0.55, h*0.35), (w*0.59, h*0.36), (w*0.56, h*0.38)], fill=(30, 25, 30, 255))
    draw.ellipse([w*0.55, h*0.355, w*0.57, h*0.375], fill=(255, 255, 255, 255))

    # Arched Eyebrows
    draw.line([(w*0.39, h*0.33), (w*0.47, h*0.32)], fill=(50, 40, 40, 255), width=3)
    draw.line([(w*0.53, h*0.32), (w*0.61, h*0.33)], fill=(50, 40, 40, 255), width=3)

    # Cherry Tint Lips
    draw.line([(w*0.47, h*0.46), (w*0.53, h*0.46)], fill=(210, 50, 80, 255), width=4)

    im = im.convert('RGB')
    im.save('lady_char.png')
    print('lady_char.png created successfully!')

create_doctor_portrait()
create_court_lady_portrait()

from django.shortcuts import render
from apps.users.auth_wrapper import logged
import qrcode
from PIL import Image
from django.conf import settings


@logged
def GenereteQRView(request):

    generate = False

    if request.method == 'POST':
        logo = Image.open(settings.BASE_DIR / 'static/assets/images/logo.jpeg')
        basewidth = 100
        wpercent = (basewidth/float(logo.size[0]))
        hsize = int((float(logo.size[1])*float(wpercent)))
        logo = logo.resize((basewidth, hsize), Image.LANCZOS)
        QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
        QRcode.add_data(request.POST['url'])
        QRcode.make()
        QRcolor = '#10ac84'
        QRimg = QRcode.make_image(fill_color=QRcolor, back_color='white').convert('RGB')
        pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
        QRimg.paste(logo, pos)
        QRimg.save('./static/last_qr.png')
        generate = True


    return render(request, 'qrcodes/index.html', {'generated': generate})
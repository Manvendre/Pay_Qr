from flask import Flask, render_template,request,session,redirect
import qrcode

app = Flask(__name__)

@app.route("/" ,methods = ['GET', 'POST'])
def home():
    if(request.method=='POST'):
        upi_id = "imthemanav@paytm"  # Replace with your UPI ID
        amount = request.form.get('name')
        note = "Payment for XYZ"

        payment_url = f"upi://pay?pa={upi_id}&pn=Receiver's%20Name&mc=1234&tid=123456&tr=987654321&tn={note}&am={amount}"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            border=4,
                    )
        qr.add_data(payment_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("static/payment_qr.png")  # Save the QR code to a file
        return render_template('qd.html', {"Refesh": 1, "http://localhost"})
    else:
        return render_template('index.html')

@app.route("/uid" ,methods = ['GET', 'POST'])
def uid():
    return render_template('udi.html')



app.run(debug=True)
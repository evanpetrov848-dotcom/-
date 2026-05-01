<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>متجر علاء للعملات الرقمية</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); width: 300px; text-align: center; }
        h2 { color: #1a73e8; }
        input { width: 90%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; }
        button { width: 100%; padding: 10px; background: #1a73e8; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
        button:hover { background: #1557b0; }
        #result { margin-top: 15px; font-weight: bold; color: #333; }
    </style>
</head>
<body>

<div class="card">
    <h2>منصة علاء USDT</h2>
    <p>السعر الحالي: 1 USDT = 550 SDG</p>
    <input type="number" id="amount" placeholder="أدخل كمية USDT">
    <button onclick="calculate()">احسب التكلفة</button>
    <div id="result"></div>
</div>

<script>
    function calculate() {
        let amount = document.getElementById('amount').value;
        let rate = 550;
        let total = amount * rate;
        if (amount > 0) {
            document.getElementById('result').innerHTML = "المطلوب دفعه: " + total + " جنيه سوداني";
        } else {
            document.getElementById('result').innerHTML = "الرجاء إدخال كمية صحيحة";
        }
    }
</script>

</body>
</html>

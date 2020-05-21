import datetime
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div>
        <div class="nav_bar centered">
            <h1>Breathe Code Photo Feed</h1>
        </div>
    </div>
    <div>
        <div class="post centered">
            <div class="header">
                <div>
                    <h2>My first photo</h2>
                </div>
                <div>
                    <h2>{str(datetime.date.today())}</h2>
                </div>
            </div>
            <div class="image">
                <img src="data:image/jpeg;base64,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"/>
            </div>
            <div class="caption">
                <p>This is a photo of a cute micro pig. I didn't have a special liking for pigs when I was younger but people always send me pictures of pigs since my name is Ham. Now I think pigs are cute.</p>
            </div>
        </div>
    </div>
</body>
</html>
""")
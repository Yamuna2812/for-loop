items=["dose","idli","bisibelebath","pongal","palav","poori","chitranna"]
name=input("Enter a item")
for item in items:
    if item==name:
        print("available")
        break
else:
    print("not available")
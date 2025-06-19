# แยกข้อความ
radio_data = "HS1ABC,14.205,100,USB,Normal"
# แยกข้อมูล
parts = radio_data.split(",")

call_sign = f"นามเรียกขาน  {str(parts[0])}"
frequenzy = float(parts[1])
power = int(parts[2])
mode = str(parts[3])
status = str(parts[4])
print(call_sign)
 

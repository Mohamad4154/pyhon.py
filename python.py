# مقدار x را برابر ۱۰ قرار می‌دهد و آن را چاپ می‌کند
x = 10
print(x)

# ذخیره تعداد دانشجویان و چاپ آن
student_count = 30
print(student_count)

# ذخیره یک مقدار بولی (True) و چاپ آن
is_published = True
print(is_published)

# ذخیره نام دوره و چاپ آن
course_name = "mohamad"
print(course_name)

# ذخیره نام دوره و چاپ آن
course = "mohamad"
print(course)

# ذخیره پیام و چاپ آن
message = "mohamad"
print(message)

# ترکیب دو رشته و چاپ نتیجه
first = "hello mohamad"
seperator = " "
last = "goo too de rest room"
full = first + seperator + last
print(full)

# تبدیل نام دوره به حروف بزرگ و چاپ آن
course = "mohamad"
course_capital = course.upper()
print(course_capital)

# تبدیل نام دوره به حروف کوچک و چاپ آن
course = "GOO TOO"
print(course.lower())

# تبدیل اولین حرف نام دوره به حرف بزرگ و چاپ آن
course = "ali"
print(course.title())

# حذف فاصله‌های اضافی از دو طرف رشته و چاپ نتیجه
course = " mohsen "
print(course.strip())

# محاسبه طول رشته و چاپ آن
course = "not seperator"
print(len(course))

# جایگزینی 'n' با 'm' در رشته و چاپ نتیجه
course = "noo"
print(course.replace("n", "m"))

# بررسی وجود 'n' در رشته و چاپ نتیجه
course = "moamadf"
print("n" in course)

# یافتن اولین موقعیت 'l' در رشته و چاپ آن
course = "volvo"
print(course.find("l"))

# ایندکس
s = "mohamad"
print(s[0])


s = "mohamad"
print(s[-3])

s = "mohamad"
print(s[2:5])

s = "mohamad"
print(s[-2:-5])

s = "mohamad"
print(s[ :5])

s = "mohamad"
print(s[1: ])

s = "mohamad"
print(s[ : ])

s = "mohamad"
print(s[0:2] +s [5: ])

s = "mohamad"
print(s[0:4:2])

s = "mohamad"
print(s[::2])

s = "mohamad"
print(len(s))

s = "mohamad"
print(s[::-1])

s = "mohamad"
print(len(s))

s = "mohamad"
s = s.upper()

s = "MOHAMAD"
s = s.lower()

s = "mohamad"
s = s.count("h")
print(s)

s = "mohamad"
print(s.endswith("i"))

s = "mohamad"
print(s.startswith("r"))

s = "mohamad"
print(s.find("a"))

s = "mohamad"
print(s.isalnum())

s = "mohamad"
print(s.isnumeric())

x = "mohamad"
names = ["ali", "mohsen"]
result = x.join(names)
print(result)


s = "mohamad, ali, hosin"
print(s.split(" , "))

s = "mohamad"
print(s.replace(" ", "******"))

s = " +++++  mohamad   "
print(s.strip("+"))

s = "mohamad"
print(s.strip("+"))

s = "mohamad+++++"
print(s.rstrip("+"))

s = "mohamad"
print(s.capitalize())

# انجام عملیات‌های ریاضی و چاپ نتایج
print(2 + 2)
print(2 - 2)
print(2 * 2)
print(2 // 2)
print(2 % 2)
print(2 ** 2)
print(2 / 2)

# ضرب مقدار x در ۲۰ و چاپ نتیجه
x = 20
x = x * 20
print(x)

# گرد کردن عدد و چاپ نتیجه
print(round(2.3))

# استفاده از تابع math.ceil برای گرد کردن به بالا و چاپ نتیجه
import math
print(math.ceil(3.2))

# دریافت ورودی از کاربر و افزودن ۱ به آن و چاپ نتیجه
x = input("x: ")
y = int(x) + 1
print(y)

# دریافت نام و نام خانوادگی از کاربر و چاپ پیام خوش‌آمدگویی
first_name = input("your first name: ")
last_name = input("your last name: ")
print(f"friya {first_name} hello {last_name}")

# محاسبه مساحت و محیط مستطیل با استفاده از ورودی‌های کاربر و چاپ نتایج
tool = float(input("Enter length: "))
arz = float(input("Enter width: "))
masahat = tool * arz
mohit = (tool + arz) * 2
print("Masahat: ", masahat, "Mohit: ", mohit)

# بررسی سن و چاپ پیام مناسب
age = 15
if age >= 10:
    print("yes")
else:
    print("noo")

# استفاده از عبارت شرطی سه‌تایی برای چاپ پیام مناسب بر اساس سن
age = 20
message = "mohamad" if age >= 17 else "noo noder"
print(message)

# بررسی شرایط درآمد و اعتبار و دانشجو نبودن و چاپ پیام مناسب
high_income = True
good_credit = True
student = True
if high_income and good_credit and not student:
    print("hit")
else:
    print("byby")

# استفاده از حلقه for برای چاپ اعداد از ۰ تا ۹۹
for number in range(100):
    print("12")
    print(number)

# استفاده از حلقه for برای چاپ نقاط و اعداد از ۱ تا ۵
for number in range(5):
    print((number + 1) * ".")
    print(number + 1)

# استفاده از حلقه تو در تو برای چاپ مختصات x و y
for x in range(4):
    for y in range(2):
        print(f"({x}, {y})")

# استفاده از حلقه for برای چاپ هر کاراکتر از رشته "mohamad"
for x in "mohamad":
    print(x)

# ایجاد یک لیست و چاپ آن
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)

# استفاده از حلقه for برای چاپ هر عدد از لیست
for x in numbers:
    print(x)

# استفاده از حلقه while برای چاپ اعداد تا زمانی که بیشتر از ۰ هستند
number = 100
while number > 0:
    print(number)
    number //= 2
print("neon")

# تعریف یک تابع و چاپ پیام
def greet():
    print("mosu")
greet()

# تعریف یک تابع با ورودی‌های first_name و last_name و چاپ پیام خوش‌آمدگویی
def greet(first_name, last_name):
    print(f"hello {first_name}, {last_name}")
greet("mohamad", "ghorbani")

# تعریف یک تابع با ورودی‌های first_name و last_name و بازگشت پیام خوش‌آمدگویی
def greet(first_name, last_name):
    return f"hi {first_name} {last_name}"
message = greet("mohamad", "ghorbani")
print(message)

# تعریف یک تابع با ورودی first_name و بازگشت پیام خوش‌آمدگویی
def get_greeting(first_name):
    return f"hi {first_name}"
message = get_greeting("mohamad")
print(message)

# تعریف یک تابع با ورودی‌های number و by و بازگشت مجموع آن‌ها
def increment(number, by):
    return number + by
print(increment(number=4, by=9))


# اضافه کردن یک به عدد ورودی (با مقدار پیش‌فرض 1)
def increment(number, by=1):
    return number + by

print(increment(5))  # خروجی: 6

# یک تابع که عملیات ضرب چهار عدد را انجام می‌دهد
def multiply(x, y, z, w):
    return x * y * z * w

print(multiply(2, 4, 5, 5))  # خروجی: 200

# تابعی که آرگومان‌های ورودی را چاپ می‌کند
def multiply(*numbers):
    print(numbers)

print(multiply(1, 2, 3, 4, 5, 6, 7))  # خروجی: (1, 2, 3, 4, 5, 6, 7)

# تابعی که هر عدد از لیست ورودی را جداگانه چاپ می‌کند
def multiply(*numbers):
    for number in numbers:
        print(number)

print(multiply(1, 2, 3, 4, 5, 67, 8, 8, 9))

# تابعی که حاصل ضرب همه اعداد ورودی را برمی‌گرداند
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(1, 2, 3, 4, 5, 6, 7, 8, 9))  # خروجی: 362880

# ذخیره اطلاعات کاربر به صورت دیکشنری
def save_user(**user):
    print(user)

save_user(id=56678, name="mohamad", age=16)



def save_user(**user):
    print(user["name"])

save_user(id=867936, name="ali", age=34)


number =  list("mohamad")
print(number)

s = "a l i m o h a m a d i"
s = s.split(" ")
print(s)

x = [1, 2, 3,  5, 8, 9]
print(x[0])


x = [1, 2, 3,  5, 8, 9]
print(x[5])

x = [1, 2, 3,  5, 8, 9]
print(x[:])

x = [1, 2, 3,  5, 8, 9]
print(x[1:3])


l = 5
l2 = l * 2
print(l2)



l = [1, 2, 3, 5, "reza"]
l = l + ["a", "b"]


x = [1, 2, 3, 4, 5, 6]
x[1] = 10
print(x)


x = [1, 2, 3, 4, 5 ,"mohamad"]
y = [1, 2, 3, 4, 5 ,"ali"]
print(x == y)


x = [1, 2, 3, 4, 5 ,"mohamad"]
y = [1, 2, 3, 4, 5 ,"ali"]
print("mohamad" is x)


x = [1, 2, 3, ["a", "b"]]
print(x)


x = [1, 2, 3, ["a", "b"]]
print(x[3])


x = [1, 2, 3, ["a", "b"]]
print(x[3][1])


x = [1, 3, 6, 8, 9]
x.append(["a", "b", "c"])
print(x)


x = [1, 3, 6, 8, 9]
x[2:5] = ["a", "b"]
print(x)


x = [1, 3, 6, 8, 9]
del x[4]
print(x)


x = [1, 3, 6, 8, 9]
print(len(x))


x = [1, 3, 6, 8, 9, 7]
print(x[0:len(x)])


x = [1, 3, 6, 8, 9, 7]
print(x[0:len(x)-1])


*a, b, c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 3, 2, 4, 4575]
print(c)


# ایجاد لیستی از اعداد
numbers = list(range(1, 50))
print(numbers)

numbers = list(range(1, 50, 2))
print(numbers)

# تبدیل رشته به لیست حروف
chars = list("mohamad")
print(chars)

# محاسبه طول لیست
print(len(chars))

# جمع کردن مقدار اولین عنصر لیست
letters = [1, 2, 3]
letters[0] += 1
print(letters)

# چاپ اعداد زوج
numbers = list(range(20))
print(numbers[::2])

# جابجایی مقدارهای لیست به متغیرهای جداگانه
numbers = [1, 2, 3]
first, second, third = numbers
print(first, second, third)

# چاپ هر عنصر از لیست حروف
letters = ["a", "b", "c"]
for letter in letters:
    print(letter)

# استفاده از enumerate برای دسترسی به ایندکس و مقدار
letters = ["a", "b", "c"]
for index, letter in enumerate(letters):
    print(index, letter)

# اضافه کردن عنصر جدید به لیست
letters = ["a", "b", "c"]
letters.append("d")
print(letters)

# درج یک عنصر در مکان مشخصی از لیست
letters = ["a", "b", "c"]
letters.insert(2, "d")
print(letters)

# حذف آخرین عنصر لیست
letters = ["a", "b", "c"]
letters.pop()
print(letters)

# ذخیره و چاپ آخرین عنصر حذف شده
letters = ["a", "b", "c"]
result = letters.pop()
print(result)

# حذف عنصر مشخص شده با ایندکس
letters = ["a", "b", "c"]
result = letters.pop(1)
print(result)

# حذف عنصر مشخص شده با مقدار
letters = ["a", "b", "c"]
letters.remove("b")
print(letters)

# حذف اولین عنصر با مقدار مشخص (در صورتی که وجود داشته باشد)
letters = ["a", "b", "c", "d", "d"]
if "d" in letters:
    letters.remove("d")
print(letters)

# حذف عنصر با استفاده از del
letters = ["a", "b", "c", "d", "d"]
del letters[0]
print(letters)

# پاک کردن کامل لیست
letters = ["a", "b", "c", "d", "d"]
letters.clear()
print(letters)

# پیدا کردن ایندکس یک عنصر
letters = ["a", "b", "c"]
print(letters.index("b"))

# شمارش تعداد تکرار یک عنصر
letters = ["a", "b", "c"]
print(letters.count("b"))

# مرتب سازی لیست 
numbers = [3, 20, 1, 7, 4]
numbers.sort()
print(numbers)
#مرتب میکند لیست رو به صورت نضولی
numbers.sort(reverse=True)
print(numbers)
# استفاده از sorted برای مرتب‌سازی بدون تغییر در لیست اصلی
print(sorted(numbers))
print(numbers)
#لیست تاپل
items = [
    ("product", 10),
    ("product", 20),
    ("product", 30)
]
items.sort()
print(items)
# مرتب‌سازی لیستی از آیتم‌ها با استفاده از کلید (key)
items = [
    ("product1", 12),
    ("product2", 45),
    ("product3", 10)
]
items.sort(key=lambda item: item[1])
print(items)

# استفاده از map برای تغییر مقدارهای آیتم‌ها
items = [
    ("product1", 15),
    ("product2", 34),
    ("product3", 10),
]
prices = list(map(lambda item: item[1] * 2, items))
print(prices)

# فیلتر کردن آیتم‌ها بر اساس شرط مشخص
items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

# جفت کردن لیست‌ها با استفاده از zip
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip(list1, list2)))

# مدیریت لیست‌های مرورگر
browsing = []
browsing.append(1)
browsing.append(2)
browsing.append(3)
browsing.pop()
print("reviewing", browsing[-1])
print(browsing)


browsing.pop()
browsing.pop()
if not browsing:
    print("disable")
print(browsing)


from collections import deque

# ایجاد یک deque خالی
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)

# حذف و چاپ عناصر از سمت چپ deque
queue.popleft()
print(queue)

# ایجاد deque دیگر و انجام عملیات
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)

# حذف و بررسی خالی بودن deque
queue.popleft()
queue.popleft()
queue.popleft()

if not queue:
    print("elseg")
print(queue)

# کار با tuple ها
point = (1, 2)
print(type(point))
print(point)

# تغییر نوع متغیر point و چاپ آن
point = 1
print(type(point))
print(point)

# ترکیب و تکرار tuple ها
point = (1, 2) + (3, 4)
print(type(point))
print(point)

point = (1, 2) * 2
print(type(point))
print(point)

# بررسی انواع و چاپ لیست‌ها
point = 1
print(type(point))
print(point)

mylist = [1, 2]
print(type(mylist))
print(type(point))
print(point)

# دسترسی به عناصر لیست
point = [1, 2, 3, 4]
print(point[0])
print(point)

# تجزیه عناصر tuple
point = (1, 2, 3)
x, y, z = point
print(x, y, z)

# بررسی عضویت در tuple
point = (1, 2, 3)
if 1 in point:
    print("else")

# جابه‌جایی مقادیر بین متغیرها
x = 10
y = 20

z = x
x = y
y = z
print("x", x)
print("y", y)

# کار با آرایه‌ها
from array import array
numbers = array("i", [1, 2, 3])
print(numbers)

# استفاده از مجموعه‌ها برای پیدا کردن اعداد یکتا
numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
print(uniques)

# اضافه کردن عناصر به مجموعه
numbers = [1, 1, 2, 3, 4]
second = {1, 5}
second.add(4)
print(second)

#عملیات اجتماع
# تعریف لیستی از اعداد و تبدیل آن به یک مجموعه
numbers = [1, 1, 2, 3, 4, 5]
first = set(numbers)
second = {1, 5}
print(first | second)
#عملیات اشتراک
# تعریف لیستی دیگر از اعداد و تبدیل آن به مجموعه
numbers = [1, 1, 2, 3, 4, 4]
first = set(numbers)
second = {1, 5}
print(first & second)
#عملیات تفاوت
# تعریف لیستی دیگر از اعداد و تبدیل آن به مجموعه
numbers = [1, 1, 2, 3, 4, 4]
first = set(numbers)
second = {1, 5}
print(first - second)
#عملیات تفاوت متقارن
# تعریف لیستی دیگر از اعداد و تبدیل آن به مجموعه
numbers = [1, 1, 2, 3, 4, 5]
first = set(numbers)
second = {1, 5}
print(first ^ second)

# تعریف لیستی دیگر از اعداد و تبدیل آن به مجموعه
numbers = [1, 1, 2, 3, 4, 5]
first = set(numbers)
second = {1, 5}
if 1 in first:
    print("yes")

# تعریف یک دیکشنری (نقطه) و نمایش مقدار کلید "x"
point = {"x": 1, "y": 2}
print(point["x"])

# به‌روز رسانی مقدار کلید "x" و اضافه کردن کلید "z" به دیکشنری
point = {"x": 1, "y": 2}
point["x"] = 10
point["z"] = 20
print(point)

# بررسی وجود کلید "a" در دیکشنری
point = {"x": 1, "y": 2}
point["x"] = 10
point["z"] = 20
if "a" in point:
    print(point["a"])

# نمایش مقدار کلید "i" با استفاده از متد get (بازگرداندن مقدار None اگر کلید وجود ندارد)
point = {"x": 1, "y": 2}
point["x"] = 10
point["z"] = 20
print(point.get("i"))

# حذف کلید "x" از دیکشنری و نمایش دیکشنری به‌روز شده
point = {"x": 1, "y": 2}
point["x"] = 10
point["z"] = 20
del point["x"]
print(point)

# مرور و نمایش کلیدهای دیکشنری با استفاده از حلقه
point = {"x": 1, "y": 2}
point["x"] = 10
point["z"] = 20
for x in point:
    print(x)

# مرور و نمایش مقادیر دیکشنری با استفاده از حلقه
point = {"x": 1, "y": 2}
point["x"] = 10
point["z"] = 20
for x in point:
    print(point[x])

# مرور و نمایش کلیدها و مقادیر دیکشنری با استفاده از حلقه
point = {"x": 1, "y": 2}
point["x"] = 10
point["z"] = 20
for x in point:
    print(x, point[x])


try:
    age = int(input("age: "))
except ValueError:
    print("ash tebah bod")
else:
    print("not do")


try:
    age = int(input("age: "))
except ValueError as ex:
    print(ex)
    print("ash tebah bod")
else:
    print("not do")



try:
    age = int(input("age: "))
    xfactor = 10 / age
except ValueError as ex:
    print(ex)
    print("ash tebah bod")
except ZeroDivisionError:
    print("arg age")
else:
    print("dorost zadi")




try:
    age = int(input("age: "))
    xfactor = 10/age
except (ValueError,  ZeroDivisionError):
    print("ash tebah bod")
else:
    print("ash tebah bod")


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("are cannot be 0 or less")
    return 10/age
try:
     calculate_xfactor(-1)
except Exception as ex:
    print(ex)


# کلاس Point تعریف شده و متدی برای ترسیم به نام draw اضافه شده است.
class Point:
    def draw(self):
        print("draw")

point = Point()
print(type(point))


# کلاس Point تعریف شده و بررسی می‌شود که آیا نمونه‌ای از این کلاس است یا خیر.
class Point:
    def draw(self):
        print("draw")

point = Point()
print(isinstance(point, Point))


# کلاس Point با ویژگی‌های x و y تعریف شده و متد draw این مختصات را ترسیم می‌کند.
class Point:
    def __init__(self, x, y):  
        self.x = x
        self.y = y
    
    def draw(self):
        print(f"point({self.x} , {self.y})")
    
point = Point(1, 3)
point.draw()



# دو نمونه از کلاس Point ایجاد شده و متد draw اجرا می‌شود.
class Point:
    def __init__(self, x, y):  
        self.x = x
        self.y = y
    
    def greet(self):
        print(f"Point({self.x} , {self.y})")

point = Point(3, 4)
another = Point(4, 6)

point.greet()
another.greet()


# ویژگی کلاس به نام default_color اضافه شده و مقدار آن چاپ می‌شود.
class Point:
    default_color = "red"
    def init(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        print(f"point ({self.x} , {self.y})")

point = Point(4, 6)
another = Point(5, 7)
print(Point.default_color)
print(point.default_color)



# مقدار default_color برای کلاس Point تغییر داده شده و مقدار جدید چاپ می‌شود.
class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"point ({self.x} , {self.y})")

point = Point(4, 6)
another = Point(5, 7)
Point.default_color = "blue"
print(Point.default_color)
print(point.default_color)


# مقدار default_color تنها برای شیء مشخص تغییر داده شده و نتیجه چاپ می‌شود.
class Point:
    default_color = "red"
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        print(f"point ({self.x} , {self.y})")

point = Point(4, 6)
another = Point(5, 7)

point.default_color = "blue"

print(Point.default_color)
print(point.default_color)



# ویژگی default_color برای دو شیء به مقادیر متفاوت تغییر داده شده و مقادیر چاپ می‌شود.
class Point:
    default_color = "red"
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        print(f"point ({self.x} , {self.y})")

point = Point(4, 6)
another = Point(5, 7)

point.default_color = "blue"
another.default_color = "green"
print(Point.default_color)
print(point.default_color)



class Point:
    default_color = "red"
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

    def draw(self):
        print(f"point ({self.x} , {self.y})")

point = Point(4, 6)
print(point)



class Point:
    default_color = "red"
    def __init__(self, x, y):

        self.x = x
        self.y = y


    def __str__(self):
        return f"({self.x},{self.y})"

    def draw(self):
        print(f"point ({self.x} , {self.y})")


point = Point(1, 2)
print(point)



class Point:
    default_color = "red"
    def __init__(self, x, y):

        self.x = x
        self.y = y

    def str(self):
        return f"({self.x},{self.y})"

    def draw(self):
        print(f"point ({self.x} , {self.y})")

point = Point(1, 2)
print(str(point))



# کد ۱: eq هنوز تعریف نشده؛ بنابراین مقایسه بر اساس آدرس حافظه انجام می‌شود




# کد ۲: تعریف eq برای مقایسه برابری مقادیر x و y
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # متد eq: بررسی برابری مقادیر x و y دو شیء
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

point = Point(1, 2)
another = Point(1, 2)

print(point == another)  # نتیجه: True


# کد ۳: تعریف gt برای مقایسه "بزرگ‌تر بودن" مقادیر x و y
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# متد gt: بررسی بزرگ‌تر بودن مقادیر x و y
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

point = Point(1, 2)
another = Point(1, 2)

print(point > another)  # نتیجه: False


# کد ۴: اشتباه استفاده از gt برای عملگر کوچک‌تر
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

point = Point(1, 2)
another = Point(1, 2)

print(point < another)  # نتیجه: False



# کلاس برای نمایش یک نقطه دو بعدی
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

point = Point(3, 2)
another = Point(10, 6)

print(point + another)



class BadOfword:
    def __init__(self):  # درست کردن __init__
        self.words = {}

    def add(self, word):
        self.words[word.lower()] = self.words.get(word.lower(), 0) + 1  

document = BadOfword()
document.add("Python")
document.add("PyTHON")
document.add("pytHon")
print(document.words)

# کلاس برای پیگیری تعداد تکرار کلمات
class BadOfword:
    def __init__(self):
        self.words = {}

    def add(self, word):
        self.words[word.lower()] = self.words.get(word.lower(), 0) + 1
    
    def __getitem__(self, word):
        return self.words.get(word.lower(), 0)

document = BadOfword()
document.add("Python")
document.add("PyTHON")
document.add("pytHon")

print(document.getitem("python")) 


# کلاس با قابلیت دسترسی به کلمات مانند دیکشنری
class BadOfword:
    def __init__(self):
        self.words = {}

    def add(self, word):
        self.words[word.lower()] = self.words.get(word.lower(), 0) + 1
    
    def __getitem__(self, word):
        return self.words.get(word.lower(), 0)

document = BadOfword()
document.add("Python")
document.add("PyTHON")
document.add("pytHon")

print(document["python"])



# کلاس با قابلیت تنظیم تعداد کلمات
class BadOfword:
    def __init__(self):
        self.words = {}

    def add(self, word):
        self.words[word.lower()] = self.words.get(word.lower(), 0) + 1
    
    def __getitem__(self, word):
        return self.words.get(word.lower(), 0)
    
    def __setitem__(self, word, count):
        self.words[word.lower()] = count  

document = BadOfword()
document.add("Python")
document.add("PyTHON")
document.add("pytHon")

document["python"] = 10
print(document["python"])



# کلاس با قابلیت len و iter
class BadOfword:
    def __init__(self):
        self.words = {}

    def add(self, word):
        self.words[word.lower()] = self.words.get(word.lower(), 0) + 1
    
    def __getitem__(self, word):
        return self.words.get(word.lower(), 0)
    
    def __setitem__(self, word, count):
        self.words[word.lower()] = count  
    
    def __len__(self):
        return len(self.words)
    
    def __iter__(self):
        return iter(self.words)

document = BadOfword()
document.add("Python")
document.add("PyTHON")
document.add("pytHon")

document["python"] = 10
print(len(document))  
print(document["python"])

# کلاس با ذخیره‌سازی خصوصی برای کلمات
class BadOfword:
    def __init__(self):
        self.words = {}

    def add(self, word):
        self.__words[word.lower()] = self.__words.get(word.lower(), 0) + 1
    
    def __getitem(self, word):
        return self.words.get(word.lower(), 0)
    
    def __setitem(self, word, count):
        self.words[word.lower()] = count  
    
    def __len(self):
        return len(self.words)
    
    def __iter(self):
        return iter(self.words)

document = BadOfword()
document.add("Python")
document.add("PyTHON")
document.add("pytHon")

print(document["apple"])



# کلاس با قابلیت مدیریت قیمت
class Poroduct:
    def __init(self, price):
        self.price = price
    
    @property
    def price(self):
        return self.price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("prise no not error ")
        self.__price = value

product = Poroduct(10)
print(product.price)



# کلاس‌های والد و فرزند برای حیوانات
class Animal:
    def __init(self):  
        self.Age = 543
        
    def eat(self):
        print("eat")

class Mammel(Animal):
    def eat(self):
        print("eat")
    
    def walk(self):
        print("walk")

class Fish(Animal):
    def eat(self):
        print("eat")

age = Mammel()
print(age.Age)



# بررسی ارث‌بری والد و فرزند
class Animal:
    def init(self):  
        self.age = 543
        
    def eat(self):
        print("eat")

class Mammel(Animal):
    def eat(self):
        print("eat")
    
    def walk(self):
        print("walk")

m = Mammel()
print(m.age)  
print(isinstance(m, Animal))
print(issubclass(Mammel, Animal))



# استفاده از super در کلاس فرزند
class Animal:
    def init(self): 
        print("animal") 
        self.age = 3
    
    def eat(self):
        print("eat")

class Mammel(Animal):
    def init(self):
        super().init()
        print("animal")
        self.weight = 4  

    def eat(self):
        print("walk")
    
m = Mammel()
print(m.weight)



# مثال چندریختی با چندین ارث‌بری
class Employee:
    def greet(self):
        print("Employee greet no not")

class Person:
    def greet(self):
        print("Person, Greet")

class Manager(Employee, Person):
    pass

manager = Manager()
manager.greet()



# ترتیب معکوس در چندین ارث‌بری
class Employee:
    def greet(self):
        print("Employee greet no not")

class Person:
    def greet(self):
        print("Person, Greet")

class Manager(Person, Employee):
    pass

manager = Manager()
manager.greet()



# کلاس رشته سفارشی با متد تکرار
class Text(str):
    def duplicate(self):
        return self + self

text = Text("python")
print(text.duplicate())



# لیست سفارشی با ردیابی اپندها
class TrackableList(list):
    def append(self, object):
        print("append called")
        super().append(object)

my_list = TrackableList()
my_list.append("1")
print(my_list)



# کلاس برای مقایسه تساوی نقاط
class Point:
    def init(self, x, y):
        self.x = x
        self.y = y
    
    def eq(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)

print(id(p1))
print(id(p2))
print(p1 == p2)



import json
users = [
    {"id": 1, "name": "pedram", "age": 25},
    {"id": 2, "name": "reza", "age": 30},
    {"id": 3, "name": "mohamad", "age": 25}
]
data = json.dumps(users)
print(data)



#arrays ===> #list, tuple, set, dict
list1 = ["hello", "goodbye", 12, 0.5]
tupel = ("lohn", "ali", 100, False)
set1 = {"mohamad", 50, True}
dect1 = {"name":"mohamad", "lastname":"ghorbani"}


number = float(input("addad ro vared con: "))
if number > 0 :
    if number % 2 == 0 :
        print("adad mosbat v zoj ast")
    else:
        print("adad mosbat v fard ast")
elif number == 0 :
    print("adad sefr v zoj ast")
else:
    if number % 2 == 0:
        print("ada manfi v zoj ast")
    else:
        print("adad manfi v fard ast")

 
print(ord("A"))

print("char: /u0489")

print("char: /U0489")

print("char: /xu0489")

print("char:/n mohamad")

print("char: /r0489")

print("char: /t0489")


x = "mohamad"
y = 4.7664
print(f"x is {x}/my is {y}/nz is {5 ** 2}")


x = [1, 3, 6, 8, 9]
x.append(["a", "b", "c"])
print(x)


x = [1, 3, 6, 8, 9]
x[2:5] = ["a", "b"]
print(x)


x = [1, 3, 6, 8, 9]
del x[4]
print(x)


x = [1, 3, 6, 8, 9]
print(len(x))


x = [1, 3, 6, 8, 9, 7]
print(x[0:len(x)])


x = [1, 3, 6, 8, 9, 7]
print(x[0:len(x)-1])


*a, b, c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 3, 2, 4, 4575]
print(c)


number =  list("mohamad")
print(number)

s = "a l i m o h a m a d i"
s = s.split(" ")
print(s)

x = [1, 2, 3,  5, 8, 9]
print(x[0])


x = [1, 2, 3,  5, 8, 9]
print(x[5])

x = [1, 2, 3,  5, 8, 9]
print(x[:])

x = [1, 2, 3,  5, 8, 9]
print(x[1:3])


l = 5
l2 = l * 2
print(l2)



l = [1, 2, 3, 5, "reza"]
l = l + ["a", "b"]

x = [1, 2, 3, 4, 5, 6]
x[1] = 10
print(x)

x = [1, 2, 3, 4, 5 ,"mohamad"]
y = [1, 2, 3, 4, 5 ,"ali"]
print(x == y)

x = [1, 2, 3, 4, 5 ,"mohamad"]
y = [1, 2, 3, 4, 5 ,"ali"]
print(y is x)


x = [1, 2, 3, ["a", "b"]]
print(x)

x = [1, 2, 3, ["a", "b"]]
print(x[3])

x = [1, 2, 3, ["a", "b"]]
print(x[3][1])


x = (1, 2, 3, "reza", [1, 2, 3], (6, 9, 10))

t = 1, 2, 3, 4, 5
l = [1, 2, (11, 2, 3, 4, 6, 10)]

t = 1, 2, 3, 4
print(t * 2)

t = 1, 2, 3, 4
print(t[0:3])


t = (1, 2, [3, 6, 8], 3, 4)
t[2][0] = 0
print(t)


t = (1, 2, 3)
l = list(t)
l[0] = 0
t = tuple(l)
print(l)


t = 1, 2, 3, 4, 5, 6
print(t)


t1 = (1, 2, 3, 4, 5)
t2 = t1
print(id(t1))
print(id(t2))

# دیکشنری
d = {"a": 1, "b": 2}
print(d)


d = {"a": 1, "b": 2}
print(d["b"])


d = {"a": 1, "b": 2}
print(d[1])


d = {"a": [1, 2, 3], "b": 10}
print(d["a"])


# ست
s = {1, 2, 3, 4, 5, 6}
print(s)

d = {"b": 5, "a": 10}
d["c"] = 20
print(d)

d = {"b": 5, "a": 10}
print(d.keys())

d = {"b": 5, "a": 10}
print(d.values())

d = {"b": 5, "a": 10}
print(d.items())

# keys()
# values() # تایپش رو نشون میدهد
# items() مانند لیست و تاپلش میکند
# --------------------------------------

d = {"b": 5, "a": 10}
del d["b"]
print(d)


d = {"b": 5, "a": 10}
d["c"] = "mohamad"
x = d["c"]
del d["c"]
d["X"] = x
print(d)

l = [1, 8, 0, 3, 5, 1, 0]
print(sorted(l))


# برعکسش میکند
l = [1, 8, 0, 3, 5, 1, 0]
print(sorted(l, reverse=True))


d = dict([("a", 5), ("b", 10), ("c", 25)])
print(d)

d = dict(a=10, b=20, c=30)
print(d)


d = {"a":[1, 2, 3, 4, 5]}
print(d)

# -------------------------------

d = {
    "169": {"name": "reza", "age": 25},
    "171": {"name": "ali", "age": 14}
}

print(d["171"]["name"][0])



d = {
    "169": [1, 2, 3],
    "171": {"name": "ali", "age": 14}
} 
print(d["171"][2])


k = ["a", "b", "c"]
v = [1, 2, 3]
i = zip(k, v)
print(list(i))



k = ["a", "b", "c"]
v = [1, 2, 3]
d = dict(zip(k, v))
print(list(d))


s = {1, 5, 6, 9}
s.add(10)
print(s)


s = set([1, 1, 2, 3])
print(s)


s = {1, 2, "reza", 4.36}
s.discard("reza")
print(s)


s = {""}
i = input("name: ")
x = input("name: ")
z = input("name: ")

s.add(i)
s.add(x)
s.add(z)
print(s)


# تفاوت نیستند
P = {3, 9, 15, 12, 6, 18}
Q = {12, 18, 6, 10, 4, 16, 2, 8, 14}
print(P - Q)

# print(P.sifference(Q))

# بین دو مجموعه
P = {3, 9, 15, 12, 6, 18}
Q = {12, 18, 6, 10, 4, 16, 2, 8, 14}
print(P | Q)

# اشتراک
P = {3, 9, 15, 12, 6, 18}
Q = {12, 18, 6, 10, 4, 16, 2, 8, 14}
print(P & Q)

# تفاوت تقارن
P = {3, 9, 15, 12, 6, 18}
Q = {12, 18, 6, 10, 4, 16, 2, 8, 14}
print(P ^ Q)

# زیر مجموعه هست یا نه
P = {3, 9, 15, 12, 6, 18}
Q = {12, 18, 6, 10, 4, 16, 2, 8, 14}
print(P < Q)



x = 5
y = 10
print(x < y and x == 5)

x = 5
y = 10
print(x < y or x == 5)

mark = int(input("mark: "))
if mark < 10:
    print("rejected!")
else:
    print("Acceptied")




mark = int(input("x: "))

if mark <= 20 and mark >= 15:
    print("A")
elif mark <= 15 and mark >= 10:
    print("B")
elif mark <= 10 and mark >= 5:
    print("C")
elif mark < 5 and mark >= 0:
    print("D")
else:
    print("Error type")



# ______________2______________
mark = int(input("x: "))

if 15 <= mark <= 20:
    print("A")
elif 10 <= mark < 15:
    print("B")
elif 5 <= mark < 10:
    print("C")
elif 0 <= mark < 5:
    print("D")
else:
    print("Error type")



x = int(input("Enter: "))
if x > 5:
    print("yes")
elif x == 2:
    print("hi")
else:
    print("Error")



x = int(input("Enter: "))
if x > 5:
    print("yes: ")
if x == 7:
    print("noo!")
elif x < 10:
    print("not noo!")



x = int(input("Enter: "))
if x > 5:
    print("neda")
    if 15<= x <= 20:
        print("A")
    elif 10 <= x < 15:
        print("B")
else:
    print("not Error noo")


# _______________________________
y = 25
x = 10 + 2 if y < 20 else 5
print(x)
# _______________________________

x = int(input("x: "))
if x % 2 == 0:
    print("zoj ast")
else:
    print("fard ast")



x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
Min = x
if y < Min:
    Min = y
if z < Min:
    Min = z
print(Min)


#___________________________________________________________
# کوچک ترینش رو پیدا میکند
print(min(1, 2, 3, 4, 5, 6, 6, 7, 8))

print(min[1, 2, 3, 4, 5, 6, 6, 7, 8], default=567)
#__________________________________________________________
# بزرگ ترینش رو نشون میدهد
print(max(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
#_____________________________________________
# جمع میکند
print(sum([1, 2, 3, 4, 7, 5, 6, 4, 9]))
#______________________________________________

# حلقه ها یا فالس یا تروو هست
#word = 0
#while word <= 10:
#    print("hello")

#word = 0
#while True:
#    print("hello")


#word = 0
#while word <= 100:
#    print("hello")
#    word += 1


n = 0
while n < 100:
    print(n)
    n += 2

# از جایی که کاربر بگه اعدد زوج نشون میدهد
n = int(input("N: "))
while n < 100:
    if n % 2 == 0:
        print(n)
    n += 1

# باقیماندش به 3 و 7 بخش پزیر باشد
n = 1
while n < 1000:
    if n % 3 == 0 and n % 7 == 0:
        print(n)
    n += 1


row = 1
while row <= 5:
    print("*" * row)    
    row += 1


row = 1
n = int(input("n: "))
while row <= n:
    print("*" * row)    
    row += 1


n = int(input("n: "))
while n >= 1:
    print("*" * n)    
    n -= 1


# مقسوم علیه های عددی که کاربرم بزنه حساب میکند
n = int(input("Enter number: "))  
i = 1
while i <= n:
    if n % i == 0:
        print(i)
    i += 1


# مقسوم علیه های عددی که کاربرم بزنه حساب میکند
n = int(input("Enter number: "))
i = 1
while i <= n:
    if n % i == 0:
        print(i, end=" ")
    i += 1


# مقسوم علیه هایی که کاربر میزند رو داخل لیست قرار بدهیم
n = int(input("Enter number: "))
i = 1
l = []
while i <= n:
    if n % i == 0:
        l.append(i)
    i += 1
print(l)


# نشون میدهد عدد کامل هست یا نه
n = int(input("Enter number: "))
i = 1
l = []
while i < n:
    if n % i == 0:
        l.append(i)
    i += 1

if  sum(l)-n == n:
    print("yes!")
else:
    print("noo!")


# سری فیبوناچی
i = 1
a, b = 0, 1
while i <= 20:
    print(a)
    a, b = b, a+b
    i += 1
    

# مثال break
i = 1
while i <= 100:
    print(i)
    if i == 5:
        break    
    i += 1
print("*" * 40)


# اعددی که کاربر بزنه رو میگه کدومش کمتر هست
n = float(input("Enter a number: "))
m = n

while True:
    s = input("mighahi edame badahi: ")
    if s.lower() == "no":
        break
    n = float(input("Enter a adad: "))
    if n < m:
        m = n
    print("Smallest so far:", m) 



i = 0
while i <= 10:
    i += 1
    if i % 3 == 0:
        continue # برمیگرده به اول حلقه
    print(i)
    


i = 0
while i <= 10:
    i += 1
    if i % 3 == 0:
        break
    print(i)
else: # زمانی اجرا میشه که حلقه ی من بدون دردسر اجرا بشهbreak نخوره
    print("ok!")



n = int(input("n: "))
i = 2
if n > 1:
    while i < n:
        if n % i == 0:
            print(n, "adadi ce vared cardi adad aval nist")
            break
        i += 1
    else:
        print(n, "adad aval ast")
else:
    print(n, "adadi ce vared cardi adad aval nist")


# file ===> reza_dolati
x = [1, 3, 6, 8, 9]
x.append(["a", "b", "c"])
print(x)


x = [1, 3, 6, 8, 9]
x[2:5] = ["a", "b"]
print(x)


x = [1, 3, 6, 8, 9]
del x[4]
print(x)


x = [1, 3, 6, 8, 9]
print(len(x))


x = [1, 3, 6, 8, 9, 7]
print(x[0:len(x)])


x = [1, 3, 6, 8, 9, 7]
print(x[0:len(x)-1])


*a, b, c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 3, 2, 4, 4575]
print(c)


number =  list("mohamad")
print(number)

s = "a l i m o h a m a d i"
s = s.split(" ")
print(s)

x = [1, 2, 3,  5, 8, 9]
print(x[0])


x = [1, 2, 3,  5, 8, 9]
print(x[5])

x = [1, 2, 3,  5, 8, 9]
print(x[:])

x = [1, 2, 3,  5, 8, 9]
print(x[1:3])


l = 5
l2 = l * 2
print(l2)



l = [1, 2, 3, 5, "reza"]
l = l + ["a", "b"]

x = [1, 2, 3, 4, 5, 6]
x[1] = 10
print(x)

x = [1, 2, 3, 4, 5 ,"mohamad"]
y = [1, 2, 3, 4, 5 ,"ali"]
print(x == y)

x = [1, 2, 3, 4, 5 ,"mohamad"]
y = [1, 2, 3, 4, 5 ,"ali"]
print("mohamad" is x)


x = [1, 2, 3, ["a", "b"]]
print(x)

x = [1, 2, 3, ["a", "b"]]
print(x[3])

x = [1, 2, 3, ["a", "b"]]
print(x[3][1])


x = [1, 2, 3, ["amin", "banda"]]
print(x[3][1])


# tupel ===>  قیر قایل تقیر

x = (1, 2, 3, "reza", [1, 2, 3], (6, 9, 10))

t = 1, 2, 3, 4, 5
l = [1, 2, (11, 2, 3, 4, 6, 10)]

t = 1, 2, 3, 4
print(t * 2)

t = 1, 2, 3, 4
print(t[0:3])


t = (1, 2, [3, 6, 8], 3, 4)
t[2][0] = 0
print(t)


t = (1, 2, 3)
l = list(t)
l[0] = 0
t = tuple(l)
print(l)


t = 1, 2, 3, 4, 5, 6
print(t)


t1 = (1, 2, 3, 4, 5)
t2 = t1
print(id(t1))
print(id(t2))

# دیکشنری
d = {"a": 1, "b": 2}
print(d)


x = {"id": [588677], "b": 656}
print(x["id"])


d = {"a": [1, 2, 3], "b": 10}
print(d["a"])


# ست
s = {1, 2, 3, 4, 5, 6}
print(s)

d = {"b": 5, "a": 10}
d["c"] = 20
print(d)

d = {"b": 5, "a": 10}
print(d.keys())

d = {"b": 5, "a": 10}
print(d.values())

d = {"b": 5, "a": 10}
print(d.items())
# keys()
# values() # تایپش رو نشون میدهد
# items() مانند لیست و تاپلش میکند
# --------------------------------------

d = {"b": 5, "a": 10}
del d["b"]
print(d)


d = {"b": 5, "a": 10}
d["c"] = "mohamad"
x = d["c"]
del d["c"]
d["X"] = x
print(d)

l = [1, 8, 0, 3, 5, 1, 0]
print(sorted(l))


# برعکسش میکند
l = [1, 8, 0, 3, 5, 1, 0]
print(sorted(l, reverse=True))


d = dict([("a", 5), ("b", 10), ("c", 25)])
print(d)

d = dict(a=10, b=20, c=30)
print(d)


d = {"a":[1, 2, 3, 4, 5]}
print(d)

# -------------------------------

d = {
    "169": {"name": "reza", "age": 25},
    "171": {"name": "ali", "age": 14}
}

print(d["171"]["name"][0])



d = {
    "169": [1, 2, 3],
    "171": {"name": "ali", "age": 14}
} 
print(d["171"])


k = ["a", "b", "c"]
v = [1, 2, 3]
i = zip(k, v)
print(list(i))



k = ["a", "b", "c"]
v = [1, 2, 3]
d = dict(zip(k, v))
print(list(d))


# set ===> قابل تقیر هستند ====> عناصر تکراری نمیگیرند

s = {1, 5, 6, 9}
s.add(10)
print(s)


s = set([1, 1, 2, 3])
print(s)


s = {1, 2, "reza", 4.36}
s.discard("reza")
print(s)


s = {""}
i = input("name: ")
x = input("name: ")
z = input("name: ")

s.add(i)
s.add(x)
s.add(z)
print(s)

# تفاوت نیستند
P = {3, 9, 15, 12, 6, 18}
Q = {12, 18, 6, 10, 4, 16, 2, 8, 14}
print(P - Q)

# print(P.sifference(Q))

# بین دو مجموعه
P = {3, 9, 15, 12, 6, 18}
Q = {12, 18, 6, 10, 4, 16, 2, 8, 14}
print(P | Q)

# اشتراک
P = {3, 9, 15, 12, 6, 18}
Q = {12, 18, 6, 10, 4, 16, 2, 8, 14}
print(P & Q)

# تفاوت تقارن
P = {3, 9, 15, 12, 6, 18}
Q = {12, 18, 6, 10, 4, 16, 2, 8, 14}
print(P ^ Q)

# زیر مجموعه هست یا نه
P = {3, 9, 15, 12, 6, 18}
Q = {12, 18, 6, 10, 4, 16, 2, 8, 14}
print(P < Q)
#_______________________________________
# None ===> نمیدونیم مقدارش چیه و... 
# True__False  <==== بولین bool
#_______________________________________
x = 5
y = 10
print(x < y and x == 5)

x = 5
y = 10
print(x < y or x == 5)

mark = int(input("mark: "))
if mark < 10:
    print("rejected!")
else:
    print("Acceptied")




mark = int(input("x: "))

if mark <= 20 and mark >= 15:
    print("A")
elif mark <= 15 and mark >= 10:
    print("B")
elif mark <= 10 and mark >= 5:
    print("C")
elif mark < 5 and mark >= 0:
    print("D")
else:
    print("Error type")



# ______________2______________
mark = int(input("x: "))

if 15 <= mark <= 20:
    print("A")
elif 10 <= mark < 15:
    print("B")
elif 5 <= mark < 10:
    print("C")
elif 0 <= mark < 5:
    print("D")
else:
    print("Error type")



x = int(input("Enter: "))
if x > 5:
    print("yes")
elif x == 2:
    print("hi")
else:
    print("Error")



x = int(input("Enter: "))
if x > 5:
    print("yes: ")
if x == 7:
    print("noo!")
elif x < 10:
    print("not noo!")



x = int(input("Enter: "))
if x > 5:
    print("neda")
    if 15<= x <= 20:
        print("A")
    elif 10 <= x < 15:
        print("B")
else:
    print("not Error noo")


# _______________________________
y = 25
x = 10 + 2 if y < 20 else 5
print(x)
# _______________________________

x = int(input("x: "))
if x % 2 == 0:
    print("zoj ast")
else:
    print("fard ast")



x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
Min = x
if y < Min:
    Min = y
if z < Min:
    Min = z
print(Min)


#___________________________________________________________
# کوچک ترینش رو پیدا میکند
print(min(1, 2, 3, 4, 5, 6, 6, 7, 8))

print(min[1, 2, 3, 4, 5, 6, 6, 7, 8], default=567)
#__________________________________________________________
# بزرگ ترینش رو نشون میدهد
print(max(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
#_____________________________________________
# جمع میکند
print(sum([1, 2, 3, 4, 7, 5, 6, 4, 9]))
#______________________________________________

# حلقه ها یا فالس یا تروو هست
#word = 0
#while word <= 10:
#    print("hello")

#word = 0
#while True:
#    print("hello")


#word = 0
#while word <= 100:
#    print("hello")
#    word += 1


n = 0
while n < 100:
    print(n)
    n += 2

# از جایی که کاربر بگه اعدد زوج نشون میدهد
n = int(input("N: "))
while n < 100:
    if n % 2 == 0:
        print(n)
    n += 1

# باقیماندش به 3 و 7 بخش پزیر باشد
n = 1
while n < 1000:
    if n % 3 == 0 and n % 7 == 0:
        print(n)
    n += 1


row = 1
while row <= 5:
    print("*" * row)    
    row += 1


row = 1
n = int(input("n: "))
while row <= n:
    print("*" * row)    
    row += 1


n = int(input("n: "))
while n >= 1:
    print("*" * n)    
    n -= 1


# مقسوم علیه های عددی که کاربرم بزنه حساب میکند
n = int(input("Enter number: "))  
i = 1
while i <= n:
    if n % i == 0:
        print(i)
    i += 1


# مقسوم علیه های عددی که کاربرم بزنه حساب میکند
n = int(input("Enter number: "))
i = 1
while i <= n:
    if n % i == 0:
        print(i, end=" ")
    i += 1


# مقسوم علیه هایی که کاربر میزند رو داخل لیست قرار بدهیم
n = int(input("Enter number: "))
i = 1
l = []
while i <= n:
    if n % i == 0:
        l.append(i)
    i += 1
print(l)


# نشون میدهد عدد کامل هست یا نه
n = int(input("Enter number: "))
i = 1
l = []
while i < n:
    if n % i == 0:
        l.append(i)
    i += 1

if  sum(l)-n == n:
    print("yes!")
else:
    print("noo!")


# سری فیبوناچی
i = 1
a, b = 0, 1
while i <= 20:
    print(a)
    a, b = b, a+b
    i += 1
    

# مثال break
i = 1
while i <= 100:
    print(i)
    if i == 5:
        break    # برنامه رو تموم میکند
    i += 1
print("*" * 40)


# اعددی که کاربر بزنه رو میگه کدومش کمتر هست
n = float(input("Enter a number: "))
m = n

while True:
    s = input("mighahi edame badahi: ")
    if s.lower() == "no":
        break
    n = float(input("Enter a adad: "))
    if n < m:
        m = n
    print("Smallest so far:", m) 



i = 0
while i <= 10:
    i += 1
    if i % 3 == 0:
        continue # برمیگرده به اول حلقه
    print(i)
    


i = 0
while i <= 10:
    i += 1
    if i % 3 == 0:
        break
    print(i)
else: # زمانی اجرا میشه که حلقه ی من بدون دردسر اجرا بشهbreak نخوره
    print("ok!")



n = int(input("n: "))
i = 2
if n > 1:
    while i < n:
        if n % i == 0:
            print(n, "adadi ce vared cardi adad aval nist")
            break
        i += 1
    else:
        print(n, "adad aval ast")
else:
    print(n, "adadi ce vared cardi adad aval nist")


# حلقه های تو در تو
i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(j)
        j += 1
    print(i)
    i += 1


l = ["reza", "sahel", "ali", "saman"]
i = 0
while i < len(l):
    s = (l[i])
    j = 0
    while j < len(s):
        if j % 2 == 0:
            print(s[j].upper(), end="")
        else:
            print(s[j], end="")
        j += 1
    print()
    i += 1



l = input("Enter a clik name").split("-")
print(l)
i = 0
while i < len(l):
    s = (l[i])
    j = 0
    while j < len(s):
        if j % 2 == 0:
            print(s[j].upper(), end="")
        else:
            print(s[j], end="")
        j += 1
    print()
    i += 1

# جدول ضرب
i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(i * j, end="\t")
        j += 1
    print()
    i += 1


i = 1
while i <= 5:
    j = 1
    while j <= 1:
        print("*", end="")
        j += 1
    print()
    i += 1


# حلقه for
# l = [1, 2, 3, 4, 5, 6]
# for target in obj:
#     x-y-z-t   ===جیزی که قراره بدی به فور

list1 = [1, 2, 3, 4, 5, 6]
for x in list1:
    print(x)
# --------------------------
str = "mohamadghorbani"
for i in str:
    print(i)
# --------------------------
list1 = [34, 67, 49, 96, 57, 32, 87]
for c in list1:
    print(chr(c))


list1 = [34, 67, 49, 96, 57, 32, 87]
for x in list1:
    if x == "f":
        break
    print(chr(x))
else:
    print("OK")


list1 = [34, 67, 49, 96, 57, 32, 87]
for x in list1:
    if x == "f":
        continue
    print(chr(c))
else:
    print("OK")
# __________________________________________
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [10, 11, 12, 14, 15, 17, 5]
for i in list1:
    for j in list2:
        if i == j:
            print(i)


for a, b, c in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
    print(a, b, c)


d = {"a":1, "b": 2, "c": 3}
for key, value in d.items():
    print(key, ":", value)

# range 
print(list(range(1, 10, 2)))
# ----------------------
for i in range(50):
    print(i)
# ----------------------
l = input("Enter a name: ").split("-")
for i in l:
    print(i)
# ---------------------------------------
l = input("Enter a name: ").split("-")
print(l)
for i in range(1, len(l)):
    print(i, l[i])

# فاکتوریل
n = int(input("adade: "))
m = 1
for i in range(1, n+1):
    m *= i
print("f:", m)
# =-=-=-=-=-=-=-=-=-اینجا هستی

# رعکس میکند عدد ما رو
n = int(input("adade: "))
for i in range(len(n)-1, -1, -1):
    print(n[i], end="")
   

print(list(enumerate(["a", "b", "c", "d"])))


l = ["a", "b", "c", "d"]
for i, j in enumerate(l):
    print(i, ":", j)

# روش 1
l = ["adams", "baba", "cara", "dana"]
y = [18, 24, 37, 49]
for i in range(0, len(x)):
    print("name:", x[i], "age:", y[i])
# ---------------------------------------
# روش 2
l = ["adams", "baba", "cara", "dana"]
y = [18, 24, 37, 49]
for i, j in zip(x, y):
    print("name:", i, "age:", j)

# برعکس میکند
l = ["adams", "baba", "cara", "dana"]
y = [18, 24, 37, 49]
for i in reversed(x):
    print(x)


l = ["adams", "baba", "cara", "dana"]
y = [18, 24, 37, 49]
for i in reversed(range(10)):
    print(i)


# به ترتیب حروف الف با مرتب میکند
l = ["adams", "baba", "cara", "dana"]
y = [18, 24, 37, 49]
for i in sorted(l):
    print(i)

l = ["adams", "baba", "cara", "dana"]
y = [18, 24, 37, 49]
for i in reversed(sorted(y)):
    print(i)


# file ===> savw_tamrin
# ماشین حساب
def jem(a, b):
    return a + b

def tafrigh(a, b):
    return a - b

def zarb(a, b):
    return a * b

def taghsim(a, b):
    return a / b

def tavan(a, b):
    return a ** b

while True:
    print("amaliat ra entekhab con")
    print("1.jam")
    print("2.tafrigh")
    print("3.zarb")
    print("4.taghsim")
    print("5.tavan")
    print("6.tamam")

    user = str(input("adade amaliat ra vared konid: "))

    if user == "6":
        print("barname tamom shod")
        break 

    number1 = float(input("bazan: "))
    number2 = float(input("bezan: "))

    
    if user == "1":
        print("shod: ", jem(number1, number2))

    elif user == "2":
        print("shod: ", tafrigh(number1, number2))

    elif user == "3":
        print("shod: ", zarb(number1, number2))

    elif user == "4":
        if number2 == 0:
            print("Error")
        else:
            print("shod: ", taghsim(number1, number2))

    elif user == "5":
        print("shod: ", tavan(number1, number2))
    else:
        print("Error")
#-------------------------------------------------------------------------------
# تبدیل کیلو به گرم 
kg = int(input("Enter kg: "))
gram = kg * 1000
print("g = ", gram)



kg = int(input("Enter kg: "))
g = kg * 1000
print("g = ", g, "g")



kg = int(input("Enter kg: "))
g = kg * 1000
print("g = ", str(g)+ ("g"))



kg = int(input("Enter kg: "))
g = kg * 1000
print(g, "g",sep ="")
#----------------------------------

# مساحت مثلث 
x = int(input("Enter X: "))
y = int(input("Enter Y: "))
s = 0.5 * x * y
print("s :", s)



x = int(input("Enter X: "))
y = int(input("Enter y: "))
s = 1/2 * x * y
print("s :", s)



x = int(input("Enter X: "))
y = int(input("Enter y: "))
s = (x * y) /2
print("s :", s)
#------------------------------------


# ماشین حساب
x = int(input("Enter X: "))
y = int(input("Enter Y: "))
print(x, "+", y, "=", x + y)
print(x, "-", y, "=", x - y)
print(x, "*", y, "=", x * y)
print(x, "/", y, "=", x / y)
print(x, "**", y, "=", x ** y)



# مساحت مستتیل
tool = float(input("Enter length: "))
arz = float(input("Enter width: "))
masahat = tool * arz
mohit = (tool + arz) * 2
print("Masahat: ", masahat, "Mohit: ", mohit)
#--------------------------------------------------------
# درجه را به رادیان تبدیل میکند
d = int(input("Enter X: "))
r = d * (3.14/180)
print("R =",r)
#-------------------------------------------------
# دایره سنج
p = 3.14
r = float(input("r: "))
print("mohait: ", 2 * p * r)
print("masahat: ", p * (r ** 2))



#رندش میکند
p = 3.14
r = float(input("r: "))
print("mohait: ", round(2 * p * r))
print("masahat: ", round(p * (r ** 2)))
#---------------------------------------------


# توان سنج
x = int(input("x: "))
print("x ^ 2 =", x**2)
print("x ^ 3 =", x**3)


# توان ساز
x = int(input("x: "))
y = int(input("x: "))
print("x ** y=", x ** y)
#-------------------------------------

# میانگین سنج
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
ave = (x + y + z) / 3
print("ave =", ave)
#-----------------------------------------------------------------
# تشخیص زوج یا فرد 
number = float(input("addad ro vared con: "))
if number > 0 :
    if number % 2 == 0:
        print("adad mosbat v zoj ast")
    else:
        print("adad mosbat v fard ast")
elif number == 0 :
    print("adad sefr v zoj ast")
else:
    if number % 2 == 0:
        print("ada manfi v zoj ast")
    else:
        print("adad manfi v fard ast")
# ---------------------------------------------------
#  اون رشته هست در چیزی که کاربرم یزند
s = "hi reza is bad boy"
c = input("Enter e char: ")
print(s.count(c))
# ------------------------------
# این کد آخرین کلمه‌ی جمله‌ی ورودی رو چاپ می‌کنه.
s = input("Enter e string: ")
s = s.rstrip()
i = s.rfind(" ")
print(s[i:])
# ------------------------------
#  در جمله ی اولم متنی که زدم هست یا نه
s1 = input("Enter e string: ")
s2 = input("Enter e string: ")
print(s2 is s1)
# ------------------------------
# تمامی فاصله هارو حذو کرده
s = input("Enter e string: ")
print(s.replace(" ", ""))
# ---------------------------------
# تب هارو پاک میکند
s = input("Enter e string: ")
print(s.replace("/t", ""))
# ---------------------------------
# صفر رو پاک میکند
phone = input("x: ")
print(phone.lstrip("0"))
# ---------------------------------
# تحلیل متن
s = input("enter: ")

sentences = s.count(".") + s.count("?") + s.count("!")
words = s.count(" ") + 1
characters = len(s)
letters = characters - (s.count(".") + s.count("?") + s.count("!") + s.count(";") + s.count(":") + s.count("-") + s.count(" "))

print("aya hast dar clamatam:", sentences)
print("number of words:", words)
print("mishmarad:", characters)
print("hazv miconad:", letters)
# ----------------------------------------------------------------------------------------------------------------------------------------
# تبدیل کاراکتر به اسکی
ch = input("x: ")
print(ord(ch))
# ----------------------
# برسی میکند اسا شماره زدسد یا حروف
phone = input("phone: ")
print(phone.isnumeric())
# -------------------------------------------------
# میانگین نمرات دانش اموز
marks = []
name = input("name: ")
marks.append(name)
fizik = float(input("nomre fizik: "))
marks.append(fizik)
riazi = float(input("nomre riazi: "))
marks.append(riazi)
adabiat = float(input("nomre adabiat: "))
marks.append(adabiat)
print(marks)
ave = (marks[1] + marks[2] + marks[3]) / 3
print(ave)
# --------------------------------------------
# کودی بگیریم تعداد اون رو در رشته ذخیره کنه
phone = input("Phone: ")
digit_list = list(phone)
print(digit_list)
# -----------------------------
#
l1 = [1, 2, 3]
l2 = ["a", "b", "c"]
l1[-1] = 2  # جایگزین کردن آخرین عنصر
print(l1)

# ---------------------------------------
# 2 تا دنش جو داشته باشم اسم و نمرشو توی یه دیکشنری ذخیره کنم
marks = {}
name = input("name: ")
m = float(input("mark: "))
marks[name] = m

name2 = input("name: ")
m2 = float(input("mark: "))
marks[name2] = m2
print(marks)
# --------------------------------------------
# یه رشته بگیره از کاربر وبگه تعداد کاراکتر ها چقدره وتکراری هارو نباید بشماره
s = input("Enter string")
chs = set(s)
print(chs)
print(len(chs))
# ----------------------------------------------
# تو یه کلمه رو معنیشو میگویی
dictiomary = {}
key = input("word: ")
m1 = input("meaning1: ")
m2 = input("meaning2: ")
m3 = input("meaning3: ")
m4 = input("meaning4: ")
dictiomary[key] = [m1, m2, m3, m4]
print(dictiomary)
# ---------------------------------------
# از کاربر 2 تا شماره میگیرد
phones1 = ["0935984755", "0945845759"]
phones2 = ["0958484855", "0995598433"]
s = set(phones1 + phones2)
print(s)

phones1 = ["0935984755", "0945845759"]
phones2 = ["0958484855", "0995598433"]
s = list(set(phones1 + phones2))
print(s)
# --------------------------------------------
# به 5 و 2 بخش پذیر باشه
x = int(input("Enter number: "))
if x % 5 == 0 and x % 2 == 0:
    print("yes")
else:
    print("not noo")
# -----------------------------------------
# تشخیس 
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x < y+z and y < x+z and z < x+y:
    print("mitavanad mosalas bashad")
    if x == y and y == z and x == z:
        print("motasavi azla")
    if x == y or y == z or x == z:
        print("motasavi azla")
    if x == y and y == z and x == z:
        print("mokhtalef azla ast")
    if x ** 2 == y ** 2 + z ** 2 or y ** 2 == x ** 2 + z ** 2 or z ** 2 == y ** 2 + x ** 2:
        print("gham al zaviye")
else:
    print("nemitavanad moslas bashad")
# ---------------------------------------------------------------------------------------------------
# تشخیس عدد یا رشته
ch = input("Enter a char: ")
if ord(ch) >= 48 and ord(ch) <= 57:
    print("you caracter is number")
elif 65 <= ord(ch) <= 90 or 65 <= 90 or 97 <= ord(ch) <= 122:
    print("your charater is letter!")
else:
    print("other!")


# تشخیس عدد یا رشته
ch = input("Enter a char: ")
if 30 <= ord(ch) <= 39:
    print("you caracter is number")
elif 65 <= ord(ch) <= 90 or 65 <= 90 or 97 <= ord(ch) <= 122:
    print("your charater is letter!")
else:
    print("other!")
# -------------------------------------------------------------------------------------------


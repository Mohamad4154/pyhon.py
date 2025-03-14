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

# مرتب‌سازی لیست
numbers = [3, 20, 1, 7, 4]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

# استفاده از sorted برای مرتب‌سازی بدون تغییر در لیست اصلی
print(sorted(numbers))
print(numbers)

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
    xfactor = 10/age
except ValueError:
    print(ex)
    print("ash tebah bod")
except ZeroDivisionError:
    print("arg age")
else:
    print("ash tebah bod")


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
try: calculate_xfactor(-1)
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
another = Point(9, 6)
point.greet()
another.greet()

# ویژگی کلاس به نام default_color اضافه شده و مقدار آن چاپ می‌شود.
class Point:
    default_color = "red"
    def __init__(self, x, y):
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

    def __str__(self):
        return f"({self.x},{self.y})"

    def draw(self):
        print(f"point ({self.x} , {self.y})")

point = Point(1, 2)
print(str(point))



# کد ۱: __eq__ هنوز تعریف نشده؛ بنابراین مقایسه بر اساس آدرس حافظه انجام می‌شود
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(1, 2)
another = Point(3, 4)

print(point == another)  # نتیجه: False (زیرا __eq__ تعریف نشده است)


# کد ۲: تعریف __eq__ برای مقایسه برابری مقادیر x و y
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # متد __eq__: بررسی برابری مقادیر x و y دو شیء
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

point = Point(1, 2)
another = Point(1, 2)

print(point == another)  # نتیجه: True


# کد ۳: تعریف __gt__ برای مقایسه "بزرگ‌تر بودن" مقادیر x و y
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # متد __gt__: بررسی بزرگ‌تر بودن مقادیر x و y
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

point = Point(1, 2)
another = Point(1, 2)

print(point > another)  # نتیجه: False


# کد ۴: اشتباه استفاده از __gt__ برای عملگر کوچک‌تر
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # متد __gt__: به اشتباه برای عملگر کوچکتر استفاده شده است
    # پیشنهاد: تعریف __lt__ به جای __gt__
    def __gt__(self, other):
        return self.x < other.x and self.y < other.y

point = Point(1, 2)
another = Point(1, 2)

print(point < another)  # نتیجه: False



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



class BadOfWord:
    def __init__(self):
        self.words = {}

    def add(self, word):
        self.words[word] = self.words.get(word, 0) + 1

document = BadOfWord()
document.add("python")
document.add("python")

print(document.words)



class BadOfword:
    def __init__(self):
        self.words = {}

    def add(self, word):
        self.words[word.lower()] = self.words.get(word.lower, 0) + 1

document = BadOfword()
document.add("Python")
document.add("PyTHON")
document.add("pytHon")
print(document.words)



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




class BadOfword:
    def __init__(self):
        self.__words = {}

    def add(self, word):
        self.__words[word.lower()] = self.__words.get(word.lower(), 0) + 1
    
    def __getitem__(self, word):
        return self.__words.get(word.lower(), 0)
    
    def __setitem__(self, word, count):
        self.__words[word.lower()] = count  
    
    def __len__(self):
        return len(self.__words)
    
    def __iter__(self):
        return iter(self.__words)

document = BadOfword()
document.add("Python")
document.add("PyTHON")
document.add("pytHon")

print(document["apple"])  



class Poroduct:
    def __init__(self, price):
        self.price = price
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("prise no not error ")
        self.__price = value

product = Poroduct(10)
print(product.price)

def sweets_english(order):
    """random sweets"""
    if order == 'sweet':
        ans = ['small chocolate cake', 'marble cake', 'pumpkin bread',\
                'chocolate pound cake', 'soft pumpkin cookies', 'sugar cookies',\
                'biscoff cookies', 'red velvet cookies','tahini cookies',\
                'banana cupcakes', 'brownies', 'chocolate', 'caramel slice',\
                'chocolate coconut slice', 'easter egg rocky road',\
                'lemon slice', 'easy vanilla cheesecakes', 'sour cream cake', \
                'classic trifle', 'chocolate bread', 'vegan chocolate cake']
                #อ้างอิงเมนูจาก https://www.sweetestmenu.com/chocolate/
    elif order == 'drinks':
        ans = ['coffee', 'iced tea', 'hot chocolate', 'juice', 'milkshake', 'tea',\
                'milk', 'green tea', 'chocolate milk', 'smoothie', 'bahamas punch', \
                'spiced pineapple cooler', 'lychee spritzer', 'coconut milk',\
                'pomegranate sparkle', 'blue thyme', 'life hacker', 'orange juice',\
                'upside down blue lemonade', 'lemonade', 'cocoa', 'tea bag']
                #อ้างอิงเมนูจาก https://7esl.com/drinks-beverages-vocabulary/
    return ans

def words_english():
    """random speech"""
    words = ['Where there is good food, there is happiness : ',\
            'To live a full life, you have to fill your stomach first : ', \
            'Food is really and truly the most effective medicine : ',\
            'They told me to follow my heart. Guess where it led me? To the fridge : ',\
            'We only live once… Lick the bowl.', 'You can’t live a full life on an empty stomach : ',\
            'Come on, hog it out! : ', 'There is no “we” in fries. Remember that! : ',
            'My favorite hobby is eating : ', 'Savor the flavor : ']
            #อ้างอิงจาก https://bestreview.asia/how-to/captions-delicious-food-in-english/
    return words

def fast_food_english():
    """random fastfood"""
    fast_food = ['waffle fries', 'double-double', 'fries', 'chicken sandwich', 'curly fries',\
                'bacon cheeseburger', 'animal style burger', 'mcnuggets', 'cheesy gordita crunch',\
                'pretzel', 'spicy chicken sandwich', 'chicken tenders', 'biscuits', 'blizzard',\
                'pizza', 'glazed doughnut', 'mcgriddle', 'subway', 'church\'s chicken honey butter biscuits',\
                'panda express orange chicken', 'checkers seasoned fries', 'donut', 'big mac']
            #อ้างอิงเมนูจาก https://fastfood.theringer.com/ and https://www.eatthis.com/most-popular-fast-food/
    return fast_food

def healthfood_english():
    ans = ['Breakfast Casserole', 'Giada\'s Broiled Salmon with Herb Mustard Glaze', 'Whole30 Bacon and Egg Cups',\
        'Slow-Cooker Pork Tacos', 'Vegetable Noodle Soup', 'Angel Food Cake', 'Blueberry Compote', 'Giada\'s Chicken Saltimboccaง', \
        'Spaghetti Squash and Meatballs', 'Ellie\'s Tuscan Vegetable Soup', 'Quinoa Salad', 'Low-Cal Fettuccine Alfredo',\
        'Giada\'s Chia Seed Pudding', 'Hasselback Sweet Potatoes', ' Beef Stir-Fry', 'Gazpacho', 'Healthy Cauliflower Rice',\
        'American Macaroni Salad', 'Chicken and Broccoli Stir-Fry', 'Oven-Baked Salmon', 'Ina\'s Roasted Brussels Sprouts']
        #อ้างอิงเมนูจาก https://www.foodnetwork.com/healthy/packages/healthy-every-week/healthy-mains/foodnetwork-most-saved-healthy-recipes
    return ans

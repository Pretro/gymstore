# __GymStore__

The goal of this project is to create an e-commerce webpage that allows users to create buying orders. Users can navigate through the site and choose products to buy as they 
please. This project aims to create a real environment like that of a shopping site.

This virtual store has a profile section area which allows users to become members and save information about their purchases. You can also buy without having the need to 
become a member of the store. In the making of this project CRUD functionality where programmed in python.

In future updates, the goal is to make the store already in real mode, selling products and making payments and not only in a demo enviroment. One other more ambitious update is 
that the store will be available in other languages, this will make it possible to expand the branch of clients that visit the store. This is the fourth ms4 project from Code Institute.

# User Experience __(UX)__

## __User Stories__

As a user of this site, I want to

1. As a user, i want to be able to easily understand what the site is about so that i can decide if this is a site of my interest.

2. As a user, i want to easy navigate through the different pages so that i can use the site.

3. As a user, i want to register an account so that i can become a member.

4. As a user, i want the process of registration to be simple so that i can start make use of the site and not lose interest with registration processes that take a long time.

5. As a user, i want to view a description of the products so that i can see if it is what I am really looking for and it interests me.

6. As a user, i would like to easily be able to add products to the cart . 

7. As a user, i want to see a list of the products that I buy so that i can be able to take an order of my purchases .

8. As a user, i want to add and delete products from my shopping cart.

9. As a user, i want the checkout form to be as clear as possible. i want to see/fill my user information. See a list of what I have bought and have in my cart, the total amount to pay.

10. As a user, i want to have a safe payment alternative so that i can be sure that my card details will not fall into the wrong hands.

11. As a User, i want to receive emails with details of my purchases so that I can compare when you arrive the products that everything is received in order to how it was purchased.

12. As a User, i want to easily recover my password incase I forget it.

## __The purpose of the GymStore is to :__

+ Create an online commercial store where people can have access to buy products for exercise and nutrition.

+ Create an environment of commerce that assimilates as much as possible to reality.

+ Today online shopping is more common than before. The sale of products from different areas has become a lifestyle. Which opens a way to competition between different companies.

The idea of ​​making this online store was born from the ms4 project for Code Institute. The inspiration for this site comes from the Swedish site [gymgrossisten](https://www.gymgrossisten.com/).


### __Project Strategy__

To meet the goal of this project, the following strategy has been implemented.

+ Provide CRUD functions are included making it possible for the user to handle their information.

+ The site is built to easy navigate and this makes it also easy to use.

+ A secure checkout page where user can see a detailed list of their products

+ A registration section thus giving the option of being able to track purchases by sending emails

### __Design__

__Color Scheme__

The colours that I used for the site:

* (Black) Background color of all system templates. 

* (White) For the titles in the navbar, and for the texts in the other templates of the website such as buttons, product descriptions, etc.

* (Blue) Is used by the text box where the visa card number is placed on the checkout page

* (Green) Is the default color of the buttons in the checkout page. Also the hover color for the view button in the all product page.

* (Red) It is used for the "shop now" button and the text of the card purchase.

* (Grey) is the hover color for the add to cart button in the all product page and the color main color for the button in the product detail page.

The reason why these colors were chosen is because since the background color is black. It was necessary to use strong colors that contrast with the environment. This contrast allows the user to be more focused 
on what they need and also gives at the same time a typical atmosphere of the gym world. Since in most of these sites and from the site in which this project was inspired, the main background color is black.


### __Typography__

"Roboto" and Sans-Serif font has been used in the website. The reason why this font was chosen is because it makes the text of the site more clear. Roboto has a dual nature. It has a mechanical skeleton and the forms are largely geometric. Roboto also allows letters to be settled into their natural width. This makes the reading rhythm to be more natural.
    
### __Imagery__

The images used for the creation of this project were taken from the Swedish website [gymgrossisten](https://www.gymgrossisten.com/). The picture in the home page is from pexels.com. The reason for this choice is that being an online store for exercise products, it is important that the first impression of the user when entering is to understand what the site is about. 
The images taken from the gymgrossisten page are only use as images of the products available in the online store.

## __Wireframes__

*******

## __Features__ 

* Responsive on all devices.

* Interactive elements.

* Responsive navbar.

* Designed with HTML5, CSS, Python3, JavaScript, Bootstrap, and Django.

* Register members page where users can register.

* Login page where only register users can have access to.

* The use of stripe as a payment method for purchases.

* Product page ordered in different categories.

* The option to search products by categories, price and rating.

* Shopping cart page where users can see a list of products they have been purchased. Also manage to increase or delete the products they want.

* Checkout page where the payment is generated.

* Email sending to users with details of their purchases


## __Features left to implement in the future__

* A function that makes it possible to recover user password.

* Make it possible to have the ecommerce site in several languages, not just in english.

* Create more product areas with their categories, turning this not only into an ecommerce store but rather a kind of online gallery.

* Add another payment system such as PayPal, giving the user the option to choose the payment system that is most convenient for them.

* A map where the user can mark the cities and places he/she has visited.

* Create a function that allows to send advertasing for new products to registered users.


## __Technologies Used__

+ For the making of this project, the following technologies has been used

##### __Languages__

* [HTML5](https://en.wikipedia.org/wiki/HTML5)

* [CSS3](https://en.wikipedia.org/wiki/CSS)

* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

* [Python](https://www.python.org/)

#### __Django framework__ 

* [Django](https://www.djangoproject.com/)

  Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)

  This is used for register, sign up and sign out pages.

* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)

  Used for all forms in this project.
  
#### __Integrations__

+ [Fontawesome](https://fontawesome.com/)

  Font Awesome is a font and icon toolkit i use for the icons on different pages.

+ [Googlefonts](https://fonts.google.com/)

  Used in this project for typography.

+ [Booststrap](https://getbootstrap.com/)

  Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development. It contains CSS- and (optionally) JavaScript-based design templates for typography, forms, buttons, navigation, and other interface components.

### __Repository, workspace__

+ [Gitpod](https://www.gitpod.io/) 

  Gitpod is used as the enviroment program were the page was made and for the writing of the code.

+ [Github](https://github.com/) 

  I use Github to host the deployed website. Also in Github you can track your code and go back to previous versions to keep track of what you've done.

+ [Heroku](https://www.heroku.com/)

  Platform used for the deployments and running the apps. 

## __Resources__
 
+ [Balsamic](https://balsamiq.com/)

  Program use for the making of the wireframes for this project.
  
+ [Stripe](https://stripe.com/en-gb-se)

  I use stripe for the project payment system. In addition, it is one of the requirements of this project.

+ [YouTube](https://www.youtube.com/)

  I use this site to get inspiration from other projects and to search information about source code. 

+  [Markdown](https://guides.github.com/features/mastering-markdown/)

  Markdown is a easy-to-use syntax for styling all forms of writing on the GitHub platform.

+  [W3schools](https://www.w3schools.com/)

  I use this site to get answers to questions about the programming languages used. 
  
+ [Amazon Web Services](https://aws.amazon.com/)

  I use Amazon to store the static and media files.This procedure is performed by saving the corresponding information in the AWS S3 bucket.
  
  https://aws.amazon.com/

## The code is validated in the following pages for error correction:

+ [W3C Validator HTML](https://validator.w3.org/)

+ [JSHint](https://jshint.com/)

+ [CSS](https://jigsaw.w3.org/css-validator/#validate_by_input)

+ [Pep8](http://pep8online.com/)

+ [Reposinator](https://www.responsinator.com/)

+ [Devtool](https://developers.google.com/web/tools/chrome-devtools)


# Data schema

Django works with SQL databases by default. Sqlite3 has been used in the development environment. Instead, when deploying to Heroku, it provides a PostgreSQL database for deployment.

## __Product App__

__Product Model__

   Title                 |      Db Key             |   Data Type   |      Comments                                                              |
-----                    | -                       |             - | -                                                                          |
Category                 | category                | ForeignKey    |  on_delete=models.CASCADE                                                  |
Sku                      | sku                     | CharField     | max_length=250, blank=True                                                 |
Name                     | name                    | CharField     | max_length=250                                                             |
Description              | description             | TextField     |                                                                            |
Price                    | price                   | DecimalField  | max_digits=6, decimal_places=2                                             |
Rating                   | rating                  | DecimalField  | max_digits=6, decimal_places=2, blank=True                                 |
Image url                | image_url               | URLField      | max_length=1024, null=True, blank=True                                     |
Image                    | image                   | ImageField    | null=True, blank=True                                                      |
Stock                    | stock                   | IntegerField  | null=True, blank=True                                                      |
Has sizes                | has_sizes               | BooleanFieldv | default=True, null=True, blank=True                                        |


__Category Model__
   Title                 |      Db Key             |   Data Type   |                                 Comments                                   |
-----                    | -                       |             - | -                                                                          |
Name                     | name                    | CharField     | max_length=250                                                             |
Friendly Name            | friendly_name           | CharField     | max_length=250, blank=True                                                 |

## __Cart App__

__Cart Model__
   Title                 |      Db Key             |   Data Type   |                                 Comments                                   |
-----                    | -                       |             - | -                                                                          |
Cart id                  | cart_id                 | CharField     | max_length=250, blank=True                                                 |
Date added               | date_added              | DateField     | auto_now_add=True                                                          |

__Cart_item Model__
   Title                 |      Db Key             |   Data Type   |                                 Comments                                   |
-----                    | -                       |             - | -                                                                          |
Product                  | product                 | ForeignKey    | blank=False, on_delete=models.CASCADE                                      |
Cart                     | cart                    | ForeignKey    | on_delete=models.CASCADE                                                   |
Quantity                 | quantity                | IntegerField  |                                                                            |
Active                   | active                  | BooleanField  | default=True                                                               |

## __Checkout App__

__Order__ 
   Title                 |      Db Key             |   Data Type   |                                 Comments                                   |
-----                    | -                       |             - | -                                                                          |
Order Number             | order_number            | CharField     | max_length=35, null=False, editable=False                                  |
User Profile             | user_profile            | ForeignKey    | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'    |
Billing Name             | billingName             | CharField     | max_length=250, blank=True                                                 |
Email Address            | emailAddress            | EmailField    | max_length=250, blank=True, verbose_name='Email Adress'                    |
Phone                    | phone                   | CharField     | max_length=15, null=False, default=0                                       |
Billing Country          | billingCountry          | CountryField  | blank_label='Country *', null=False, blank=False                           |
Billing Postcode         | billingPostcode         | CharField     | max_length=250, blank=True                                                 |
Billing City             | billingCity             | CharField     | max_length=250, blank=True                                                 |
Billing Address          | billingAdress1          | CharField     | max_length=250, blank=True                                                 |
Shipping Name            | shippingName            | CharField     | max_length=250, blank=True                                                 |
Shipping Address         | shippingAddress1        | CharField     | max_length=250, blank=True                                                 |
Shipping City            | shippingCity            | CharField     | max_length=250, blank=True                                                 |
Shipping Postcode.       | shippingPostcode        | CharField     | max_length=250, blank=True                                                 |
Shipping Country         | shippingCountry         | CountryField  | blank_label='Country *', null=False, blank=False                           |
created                  | created                 | DateTimeField | auto_now_add=True                                                          |
Delivery Cost            | delivery_cost           | DecimalField  | max_digits=8, decimal_places=2, null=False, default=0                      |
Total                    | total                   | DecimalField  | max_digits=10, null=True, decimal_places=2, verbose_name='USD Order Total' |
Grand Total              | grand_total             | DecimalField  | max_digits=8, decimal_places=2, null=False, default=0                      |
Original Cart            | original_cart           | TextField     | null=False, blank=False, default=''                                        |
Stripe Pid               | stripe_pid              | CharField     | max_length=254, null=False, blank=False, default=''                        |

__Order Line Item__ 
   Title                 |      Db Key             |   Data Type   |                                 Comments                                   |
-----                    | -                       |             - | -                                                                          |
Order                    | order                   | ForeignKey    | null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems |
Product                  | product                 | ForeignKey    | null=False, blank=False, on_delete=models.CASCADE                          |
Product size             | product_size.           | CharField     | max_length=2, null=True, blank=True                                        |
Quantity                 | quantity.               | IntegerField  | null=False, blank=False, default=0                                         |
Lineitem total           | lineitem_total          | DecimalField  | max_digits=6, decimal_places=2, null=False, blank=False, editable=False    |

## __Profile App__

__User Profile__
   Title                 |      Db Key             |   Data Type   | Comments                                                                   |
-----                    | -                       |             - | -                                                                          |
User                     | user                    | OneToOneField | on_delete=models.CASCADE                                                   |
Default Phone            | default_phone           | CharField     | max_length=15, null=True, blank=True                                       |
Default Billing Address  | default_billingAdress1  | CharField     | max_length=250, blank=True                                                 |
Default Billing Country  | default_billingCountry  | CountryField  | blank_label='Country', null=True, blank=True                               |
Default Billing Postcode | default_billingPostcode | CharField     | max_length=250, blank=True                                                 |
Default Billing City     | default_billingCity     | CharField     | max_length=250, blank=True                                                 |


## Testing

   During the testing time, the following code validates are use. 

+ [W3C](https://validator.w3.org/) Validator HTML.

+ [CSS](https://jigsaw.w3.org/css-validator/#validate_by_input) validator CSS.

+ [Pep8](http://pep8online.com/) validator Python

+ [JSHint](https://jshint.com/) JavaScript


## __Testing User Stories from User Experience (UX) Section__ 

1. As a user, i want to be able to easily understand what the site is about so that i can decide if this is a site of my interest.

    i. Entering the page, there is a title, a paragraph and a picture in which it is clearly read what the site is about.

2. As a user, i want to easy navigate through the different pages so that i can use the site.

    i. The main page has a navigation menu in which there are some options. One  is a product where the categories are shown. There is also the option to search for products either by price, rating and a search engine where the user also searches by product name. 
    
    A section of entry and registration of members of the page as well as the option of shopping bag shown with an icon.

3. As a user, i want to register an account so that i can become a member.

    i. The user has the option of registering a user account in the navigation menu. Once this is done, the user is a registered member.

4. As a user, i want the process of registration to be simple so that i can start make use of the site and not lose interest with registration processes that take a long time.

    i. To register choose a username of your choice and a password. Then you can start using the site. This process avoids a delayed registration process and that the user loses interest in the site.

5. As a user, i want to view a description of the products so that i can see if it is what I am really looking for and it interests me.

    i. There are two ways to get to the product description page. The first is by pressing the "Shop now" button on the main page. The second is by going to the navigation menu and pressing the option of products. There the user can choose to go to the page of all products or view by categories.

    ii. Once on the products page press the "view" button, being directed to the product description page.

6. As a user, i would like to easily be able to add products to the cart.

    i. On the "all products" page, as well as on the product detail page, there is the "add to cart" button which allows the chosen product to be entered into the shopping cart.

7. As a user, i want to see a list of the products that I buy so that i can be able to take an order of my purchases.

    i. Once the "add to cart" button is pressed, the user is directed to the cart page a detail list of the products to buy appears.

8. As a user, i want to add and delete products from my shopping cart.

    i. On the cart page, the user also has the possibility of adding, reducing or completely eliminating the product from the shopping cart. This is achieved through icons on each product detail card.

9. As a user, i want the checkout form to be as clear as possible. i want to see/fill my user information. See a list of what I have bought and have in my cart, the total amount to pay.


# __Further Testing__

******

### __The website has been checked in different browser, such as.__

1. Chrome

2. Firefox

3. Safari

4. Microsoft edge

* The responsive part has also been tested in http://www.responsinator.com/ for

1. Ipad

2. Iphone

3. Android

4. Laptop

Friends and family tested the site by login in and writing about their stories. This was also made to point out any bugs and/or user experience issues.

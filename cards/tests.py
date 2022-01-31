from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Package, Card, Learning_statistics, CardForm
from django.http import HttpResponse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
"""Tests views and the database models"""

class IndexPageTestCase(TestCase):
    """test that index page returns a status code 200"""
    def test_index_page(self):
        """index page status code"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)




class CardsTestCase(TestCase):
    """Test cards related features"""

    def setUp(self):
        """Setup cards in the database (users, packages and cards)"""
        self.test_package_1 = Package.objects.create(name="Géo")
        self.get_package_1 = Package.objects.get(name="Géo")
        self.test_package_1 = Package.objects.create(name="Histoire")
        self.get_package_2 = Package.objects.get(name="Histoire")
        
        self.test_card_1 = Card.objects.create(
            question="Question 1",
            answer="réponse 1",
            package=self.get_package_1,
            tag="geo")

        self.test_card_2 = Card.objects.create(
            question="Question 2",
            answer="réponse 2",
            package=self.get_package_1,
            tag="geo")

        self.test_card_3 = Card.objects.create(
            question="Question 3",
            answer="réponse 3",
            package=self.get_package_2,
            tag="histoire")
        
        self.test_card_4 = Card.objects.create(
            question="Question 4",
            answer="réponse 4",
            package=self.get_package_2,
            tag="histoire") 

        self.test_card_5 = Card.objects.create(
            question="Question 5",
            answer="réponse 5",
            package=self.get_package_1,
            tag="geo") 

        self.user = User.objects.create(username="test_1", password="secret_password", is_active=1)
        self.user.save()


    def test_create_status_200(self):
        """create page status code"""
        response = self.client.get(reverse('cards:create'))
        self.assertEqual(response.status_code, 200)




    def test_learn_status_404(self):
        """Learn page status code 404 if user is doesn't exist"""
        self.client.force_login(user=self.user)
        response = self.client.get(reverse('cards:learn', kwargs={'package':self.get_package_1.name + "add a name"}))
        self.assertEqual(response.status_code, 404)

    # def test_learning_stat_status_200(self):
    #     """Learning_stat page status code"""
    #     response = self.client.get(reverse('cards:learning_stat'))
    #     self.assertEqual(response.status_code, 200)        

    def test_history_status_200(self):
        """History page status code if user is connected"""
        self.client.force_login(user=self.user)
        response = self.client.get(reverse('cards:history', kwargs={'user':self.user.id}))
        self.assertEqual(response.status_code, 200)


    def test_history_status_404(self):
        """History page status code 404 if the user doesn't exist"""
        self.client.force_login(user=self.user)
        response = self.client.get(reverse('cards:history', kwargs={'user':self.user.id + 345}))
        self.assertEqual(response.status_code, 404)

    def test_history_302(self):
        """History page status code 302 if the user is not loged"""
        response = self.client.get(reverse('cards:history', kwargs={'user':self.user.id}))
        self.assertEqual(response.status_code, 302)

class DatabaseTestCase(TestCase):
    """Tests the database tables"""
    def setUp(self):
        """Setup cards in the database (users, packages and cards)"""
        self.test_package_1 = Package.objects.create(name="Géo")
        self.get_package_1 = Package.objects.get(name="Géo")
        self.test_package_1 = Package.objects.create(name="Histoire")
        self.get_package_2 = Package.objects.get(name="Histoire")
        
        self.test_card_1 = Card.objects.create(
            question="Question 1",
            answer="réponse 1",
            package=self.get_package_1,
            tag="geo")

        self.test_card_2 = Card.objects.create(
            question="Question 2",
            answer="réponse 2",
            package=self.get_package_1,
            tag="geo")

        self.test_card_3 = Card.objects.create(
            question="Question 3",
            answer="réponse 3",
            package=self.get_package_2,
            tag="histoire")
        
        self.test_card_4 = Card.objects.create(
            question="Question 4",
            answer="réponse 4",
            package=self.get_package_2,
            tag="histoire") 

        self.test_card_5 = Card.objects.create(
            question="Question 5",
            answer="réponse 5",
            package=self.get_package_1,
            tag="geo") 

        self.user = User.objects.create(username="test_1", password="secret_password", is_active=1)
        self.user.save()
        
    def test_package_creation(self):
        package_number = Package.objects.count()
        Package.objects.create(name="Cinéma")
        assert Package.objects.count() == package_number + 1


    def test_package_delete(self):
        package_number = Package.objects.count()
        package_selected = Package.objects.get(name="Histoire")
        package_selected.delete()
        assert Package.objects.count() == package_number - 1

    def test_card_creation(self):
        """test the creation of a new card"""
        cards_number = Card.objects.count()
        Card.objects.create(            
            question="Question 6",
            answer="réponse 6",
            package= self.get_package_1,
            tag="geo")
        assert Card.objects.count() == cards_number + 1


    def test_card_delete(self):
        """test card page returns a status code 404 if the package does
        not exist"""
        cards_number = Card.objects.count()
        card_selected = Card.objects.get(question="Question 1")
        card_selected.delete()
        assert Card.objects.count() == cards_number - 1


    def test_empty_Cardform(self):
        """Test the HTML rendering of the card form"""
        self.client.force_login(user=self.user)
        reponse = self.client.get(reverse('cards:create'))
        self.assertInHTML(
            '<input type="text" name="question" maxlength="2000" required id="id_question">', 
            str(reponse.content)
            )
        # self.assertInHTML(
        #     '<select name="package" required id="id_package">',
        #     str(reponse.content)
        #     )
        self.assertInHTML(
            '<input type="text" name="answer" maxlength="2000" required id="id_answer">', 
            str(reponse.content)
            )
        self.assertInHTML(
            '<input type="text" name="tag" maxlength="200" required id="id_tag">', 
            str(reponse.content)
            )


class LearningTest(StaticLiveServerTestCase):
    """"""

    def setUp(self):
        """Setup cards in the database (users, packages and cards)"""
        self.test_package_1 = Package.objects.create(name="Géo")
        self.get_package_1 = Package.objects.get(name="Géo")
        self.test_package_1 = Package.objects.create(name="Histoire")
        self.get_package_2 = Package.objects.get(name="Histoire")
        
        self.test_card_1 = Card.objects.create(
            question="Question 1",
            answer="réponse 1",
            package=self.get_package_1,
            tag="geo")

        self.test_card_2 = Card.objects.create(
            question="Question 2",
            answer="réponse 2",
            package=self.get_package_1,
            tag="geo")

        self.test_card_3 = Card.objects.create(
            question="Question 3",
            answer="réponse 3",
            package=self.get_package_2,
            tag="histoire")
        
        self.test_card_4 = Card.objects.create(
            question="Question 4",
            answer="réponse 4",
            package=self.get_package_2,
            tag="histoire") 

        self.test_card_5 = Card.objects.create(
            question="Question 5",
            answer="réponse 5",
            package=self.get_package_1,
            tag="geo") 

        self.user = User.objects.create(username="test_1", password="secret_password", is_active=1)
        self.user.save()
      
       # create a new Firefox session


        self.driver = webdriver.FirefoxOptions()
        self.driver.headless = True
        webdriver.Firefox(options=self.driver)
        
        #local execution only
        #self.driver = webdriver.Firefox(executable_path=r'C:\\Program Files\\geckodriver\\geckodriver.exe')
        #self.driver.implicitly_wait(30)
        #self.driver.maximize_window()
        # navigate to the application home page
        #self.driver.get('%s' % (self.live_server_url))



    def test_singup(self):

        timeout = 10
        # get the search textbox required to login
        self.driver.find_element_by_name("user_i").click()
        self.driver.find_element_by_name("sign_up").click()
        self.driver.find_element_by_name("username").send_keys("test_2")
        self.driver.find_element_by_name('password1').send_keys("secret_password")
        self.driver.find_element_by_name('password2').send_keys("secret_password")
        self.driver.find_element_by_name("signup").submit()
        lists = WebDriverWait(self.driver, timeout).until(
            lambda driver: self.driver.find_element_by_name("log_in"))
        self.driver.find_element_by_name("username").send_keys("test_2")
        self.driver.find_element_by_name('password').send_keys("secret_password")
        self.driver.find_element_by_name("log_in").submit()
        self.driver.find_element_by_name("Géo").click()
#        self.driver.find_element_by_name("Géo").click()

        #get the list of elements which are displayed after the search
        #currently on result page usingfind_elements_by_name_namemethod

        self.assertEqual(self.driver.find_element_by_tag_name('h1').text, "Testez-vous")
        self.assertEqual(self.driver.current_url, self.live_server_url + reverse("cards:learn", kwargs={'package':self.get_package_1.name}))

    # def tearDown(self):
    #     # close the browser window
    #     self.driver.quit()
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith ouviu falar de uma nova aplicação
        # lista de tarefas. Ela decide verificar sua homepage
        self.browser.get('http://localhost:8000')

        # Ela percebe que o título da página e o cabeçalho mencionam list de tarefas (to-do)
        self.assertIn('to-do', self.browser.title)
        self.fail('Finish the test')

        # Ela é convidada a inserir um item de tarefa imediatamente

        # Ela digit "Buy peacock feathers" em uma caixa
        # de texto (o hobby de Edith é fazer iscas para pesca com fly)

        # Quando ela teclar enter, a página é atualizada, e agora página lista
        # "1: Buy peacock feathers" como um item em uma lista de tarefas

        # Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro
        # que o site geru um URL único para ela -- há um pequeno
        # text explicativo para isso.

        # Ela acessa esse URL - sua lista de tarefas continua lá.

        # Satisfeita, ela volta a dormir


if __name__ == '__main__':
    unittest.main(warnings='ignore')

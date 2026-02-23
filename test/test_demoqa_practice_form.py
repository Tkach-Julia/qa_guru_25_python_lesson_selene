import os

from selene import browser, be, have


def test_demoqa_practice_form():
    browser.open('https://demoqa.com/automation-practice-form')
    # ---------- Заполнить обязательные поля -----------
    browser.element('#firstName').type('Julia')
    browser.element('#lastName').type('Tkach')
    browser.element('#gender-radio-2').click()
    browser.element('#userNumber').type('1234567890')

    # ---------- Заполнить необязательные поля ----------
    browser.element('#userEmail').type('test.email@gmail.com')
    # Открываем дропдаун даты рождения и выбираем March 16th 1990
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select option[value="2"]').click()
    browser.element('.react-datepicker__year-select option[value="1990"]').click()
    browser.element('.react-datepicker__day--016').click()

    browser.element('#subjectsInput').type('Arts').press_enter()
    browser.element('#hobbies-checkbox-2').click()
    # Загрузить картинку из папки resources
    file_path = os.path.abspath('resources/artGallery.png')
    browser.element('#uploadPicture').send_keys(file_path)

    browser.element('#currentAddress').type('город Москва, ул Проспект Мира, 97').press_enter()
    # Не разобралась с выбором штата и города
    # browser.element('#state').click()
    # Кликаем на кнопку Submit
    browser.element('#submit').click()

    # --------------- Проверяем поля в форме ---------------
    browser.element('.modal-content').should(be.visible)
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    rows = browser.all('.modal-body table tbody tr')
    rows[0].all('td')[1].should(have.text('Julia Tkach'))
    rows[1].all('td')[1].should(have.text('test.email@gmail.com'))
    rows[2].all('td')[1].should(have.text('Female'))
    rows[3].all('td')[1].should(have.text('1234567890'))
    rows[4].all('td')[1].should(have.text('16 March,1990'))
    rows[5].all('td')[1].should(have.text('Arts'))
    rows[6].all('td')[1].should(have.text('Reading'))
    rows[7].all('td')[1].should(have.text('artGallery.png'))
    rows[8].all('td')[1].should(have.text(''))
    rows[9].all('td')[1].should(have.text(''))

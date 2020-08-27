@Demo
Feature: Selenium Demo
  #Esta prueba X

  Background:
    Given Read data from cell C2
    Given Read cell A2 from sheet test2
    Given Read cell A1 from sheet validacion

  Scenario: Open Browser
    Given I go to main site app
    Then close all windows

  Scenario: click
    Given I go to main site app
    And I set spotify as DOM
    And I click in element email
    And I set mervindiazlugo@gmail.com in element email
    Then close all windows

  Scenario: Dropdown Elements
    Given I open the app in https://www.correoargentino.com.ar/formularios/ondnp
    And I set correo_argentino as DOM
    And I set PU in dropdown tipo
    And wait 10 seconds
    Then close all windows

  Scenario: Assert text
    Given I go to main site app
    And I set spotify as DOM
    And I click in element email
    And I set mervindiazlugo@gmail.com in element email
    And I set TAB in element email
    Then Wait element email error
    And Assert Este correo electrónico ya está conectado a una cuenta is equal to element email error
    Then close all windows

  Scenario: Assert Element
    Given I go to main site app
    And I set spotify as DOM
    And I click in element email
    And I set mervindiazlugo@gmail.com in element email
    And I set TAB in element email
    Then Validate if this email error is present
    Then close all windows

  Scenario: Assert Element is not present
    Given I go to main site app
    And I set spotify as DOM
    And I click in element email
    And I set mervindiazlugo@gmail.com in element email
    And I set TAB in element email
    Then Validate if this email error is not present
    Then close all windows

  Scenario: by index Dropdown Elements
    Given I open the app in https://www.correoargentino.com.ar/formularios/ondnp
    And I set correo_argentino as DOM
    And set by index 2 in dropdown tipo
    And wait 10 seconds
    Then close all windows

  Scenario: Scroll
    Given I open the app in https://www.mercadolibre.com.ar/
    And I set mercadolibre as DOM
    Then scroll to element Pagar
    Then close all windows

  Scenario: click with JS
     Given I go to main site app
    And I set amazon as DOM
    Then click in element flag with JS
    And wait 10 seconds
    Then close all windows

  @openFeature
  Scenario: ScreenShots
    Given I open the app in https://www.amazon.com/
    And I set amazon as DOM
    Then Take allure ScreenShot: Hola_inMundo
    Then close all windows

  Scenario: switch to Frames
    Given I open the app in https://chercher.tech/practice/frames-example-selenium-webdriver
    And I set frames as DOM
    And I switch to Frame: frame1
    And I set hola inmundo in element Topic
    And I switch to parent frame
    Then Take a ScreenShot: switch to Frames
    And wait 3 seconds

  @openFeature
  Scenario: Accept Alerts
    Given I open the app in https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert
    And I set alerts as DOM
    And I switch to Frame: frame
    And I click in element try it
    Then Take a ScreenShot: switch to Frames
    And Accept alert present
    And wait 3 seconds


  @allure
  Scenario: Allure ScreenShots
    Given I open the app in https://www.amazon.com/
    And I set amazon as DOM
    Then Take allure ScreenShot: Hola_inMundo
    Then close all windows

  @allure
  Scenario: wait site is loaded
    Given I open the app in http://declaraciones.seniat.gob.ve/portal/page/portal/PORTAL_SENIAT
    Then Take allure ScreenShot: Hola_inMundo
    Then close all windows

   Scenario: Open new tabs
     Given I go to main site app
     Given I open new tab in: https://alt-torrent.com/
     And I go to alt-torrent tab
     Given I open new tab in: https://news.google.com/topstories?hl=es-419&gl=AR&ceid=AR:es-419
     And I go to noticias tab
     And I go to Principal tab
     And wait 10 seconds

  Scenario: move and click with actionChains
     Given I go to main site app
     And I set spotify as DOM
    And I move to email  with actionChains
    And I click in email with actionChains

  Scenario: Read From Excel
    Given Read data from cell C2
    Given Read cell A2 from sheet test2

  @openFeature
  Scenario: save in scenario context
    Given I go to main site app
    And I set spotify as DOM
    And I click in element email
    And I set mervindiazlugo@gmail.com in element email
    And I set TAB in element email
    Then Wait element email error
    And get text in element email error and save in scenario context
    Then close all windows


  @openFeature
  Scenario: Read from Scenario Context
    Given I go to main site app
    And I set spotify as DOM
    And I click in element email
    And I set Scenario:C2 in element email
    And I set TAB in element email
    Then Wait element email error
    And Assert Scenario:A1 is equal to element email error
    Then close all windows
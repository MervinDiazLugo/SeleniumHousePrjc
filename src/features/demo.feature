@Demo
Feature: Selenium Demo
  #Esta prueba X


  @openFeature
  Scenario: Open Browser
    Given I go to main site app
    Then close all windows

  @openFeature
  Scenario: click
    Given I go to main site app
    And I set spotify as DOM
    And I click in element email
    And I set mervindiazlugo@gmail.com in element email
    Then close all windows

    
  @openFeature
  Scenario: Dropdown Elements
    Given I open the app in https://www.correoargentino.com.ar/formularios/ondnp
    And I set correo_argentino as DOM
    And I set PU in dropdown tipo
    And wait 10 seconds
    Then close all windows

  @openFeature
  Scenario: Assert text
    Given I go to main site app
    And I set spotify as DOM
    And I click in element email
    And I set mervindiazlugo@gmail.com in element email
    And I set TAB in element email
    Then Wait element email error
    And Assert Este correo electrónico ya está conectado a una cuenta is equal to element email error
    Then close all windows

  @openFeature
  Scenario: Assert Element
    Given I go to main site app
    And I set spotify as DOM
    And I click in element email
    And I set mervindiazlugo@gmail.com in element email
    And I set TAB in element email
    Then Validate if this email error is present
    Then close all windows

  @openFeature
  Scenario: Assert Element is not present
    Given I go to main site app
    And I set spotify as DOM
    And I click in element email
    And I set mervindiazlugo222@gmail.com in element email
    And I set TAB in element email
    Then Validate if this email error is not present
    Then close all windows

  @openFeature
  Scenario: by index Dropdown Elements
    Given I open the app in https://www.correoargentino.com.ar/formularios/ondnp
    And I set correo_argentino as DOM
    And set by index 2 in dropdown tipo
    And wait 10 seconds
    Then close all windows

  @Navegador
  Scenario: Scroll
    Given I open the app in https://www.mercadolibre.com.ar/
    And I set mercadolibre as DOM
    Then scroll to element Pagar
    Then close all windows


  @openFeature
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
    Then Take a ScreenShot: Hola_inMundo
    Then close all windows

  @openFeature
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

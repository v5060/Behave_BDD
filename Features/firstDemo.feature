Feature: Login Functionality for newtours application


  Background:
    Given Open Browser

  @smoke
  Scenario: try to login to facebook
    When providing valid username "mercury" and password "mercury"
    Then Verifying home page

  @regression
  Scenario Outline:
    When providing valid username "<username>" and password "<password>"
    Then verify Success Message
    Examples:
      | username  | password  |
      | mercury   | mercury   |
      | adgdff    | adgdff    |

  @setupTable
  Scenario: Testing table format
    When verify login by using below query
      | username  | password  |
      | mercury   | mercury   |
    Then verifying home page



# @smoke  is  tag which we want to run as smoke test
# @regression is another tag which will run the test case as regression
# Below is the command for running tags for one or multiple tags
# behave Features\\firstDemo.feature --tags=smoke,regression
# Below is the command for only smoke tag test case to run
# behave Features\\firstDemo.feature --tags=smoke
# below is for except smoke all other tags
# behave Features\\firstDemo.feature --tags=~smoke

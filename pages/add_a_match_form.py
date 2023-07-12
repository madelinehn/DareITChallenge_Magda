from pages.base_page import BasePage

class add_a_match_form(BasePage):
    my_team_xpath ="//*[contains(@class, 'Mui-required')]"
    enemy_team_xpath = "//*[contains(@class, 'Mui-required')]"
    my_team_score_xpath = "//*[contains(@class, 'Mui-required')]"
    enemy_team_score_xpath = "//*[contains(@class, 'Mui-required')]"
    date_xpath = "//*[contains(@class, 'Mui-required')]"
    date_field_xpath = "//*[@name='date']"
    my_team_field_xpath = "//*[@name='myTeam']"
    match_at_home_button_xpath = "//*[@name='matchAtHome']"
    submit_xpath = "//*[@type='submit']"
    clear_xpath = "//*[text()='Clear']"


pass
from pages.base_page import BasePage


class Dashboard_match(BasePage):
    my_team_input_xpath = "// *[ @ name = 'myTeam']"
    enemy_team_input_xpath = "// *[ @ name = 'enemyTeam']"
    my_team_score_input_xpath = "// *[ @ name = 'myTeamScore']"
    enemy_team_score_input_xpath = "// *[ @ name = 'enemyTeamScore']"
    date_input_xpath = "// *[ @ name = 'date']"
    match_at_home_checkmark_xpath = "// child:: div/label[1]/span[2]"
    match_out_home_checkmark_xpath = "// child:: div/label[2]/span[2]"
    submit_button_xpath = "// child:: div[3] / button[1] / span[1]"
    clear_button_xpath = "// child:: div[3] / button[2] / span[1]"
    matches_button_xpath = "// child:: div / ul[2] / div[2] / div[2] / span"
    reports_button_xpath = "// child:: div / ul[2] / div[3] / div[2] / span"
    sign_out_button_xpath = "// child:: div / ul[3] / div[2] / div[2] / span"
    pass
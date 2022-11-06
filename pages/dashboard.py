from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_button_xpath = "// child::ul[1] / div[1] / div[2] / span"
    players_button_xpath = "// child::ul[1] / div[2] / div[2] / span"
    language_button_xpath = "// child::ul[2] / div[1] / div[2] / span"
    sign_out_button_xpath = "//child::ul[2]/div[2]/div[2]/span"
    add_player_button_xpath = "// child::div[2] // a[1] / button / span[1]"
    last_created_player_button_xpath = "// child::div[3] / div[3] // a[1] / button / span[1]"
    last_updated_player_button_xpath = "//child::div[3]/div[3]//a[2]/button/span[1]"
    last_created_match_button_xpath = "//child::div[3]/div[3]//a[3]/button/span[1]"
    last_updated_match_button_xpath = "//child::div[3]/div[3]//a[4]/button/span[1]"
    last_updated_report_button_xpath = "// child::div[3] / div[3] // a[5] / button / span[1]"
    dev_team_contact_button_xpath = "// child::div[1] / div[3] // a / span[1]
    pass
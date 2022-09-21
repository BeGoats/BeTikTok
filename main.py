import datetime
import random
import time
import inquirer
from colorama import init, Fore
from src import process


def main():
    init(autoreset=True)
    inject = process.ZefoyViews()
    print(
        Fore.GREEN + """
         ██████╗ ███████╗████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗
         ██╔══██╗██╔════╝╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝
         ██████╔╝█████╗     ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝ 
         ██╔══██╗██╔══╝     ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗ 
         ██████╔╝███████╗   ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗
         ╚═════╝ ╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝                                                              
                                                            TikTok Script 1.0
    """
    )
    print(Fore.LIGHTBLUE_EX + "Halo, Selamat Datang"
    )
    print(Fore.LIGHTYELLOW_EX + "Cara Menggunakannya: ")
    print(Fore.LIGHTYELLOW_EX + "1. Login akun tiktokmu di browser")
    print(Fore.LIGHTYELLOW_EX + "2. Pilih video yang akan di salin linknya")
    print(Fore.LIGHTYELLOW_EX + "3. Ubah link video tiktokmu"
    )
    print(Fore.LIGHTYELLOW_EX + "Contoh : https://www.tiktok.com/@bukanranggaya/video/7102947441078504731?is_from_webapp=1&sender_device=mobile&sender_web_id=7145515814015354370")
    print(Fore.LIGHTGREEN_EX + "Menjadi : https://www.tiktok.com/@bukanranggaya/video/7102947441078504731"
    )
    print(Fore.LIGHTRED_EX + "*Note: Jika stuck pada captcha, ketik CTRL+C lalu exit dan mulai ulang scriptnya"
    )
    url_video = input("Salin link video tiktokmu disini: ")

    questions = [
        inquirer.List('type',
                      message="Apa yang kamu inginkan?",
                      choices=['Views', 'Shares', 'Favorites'],
                      ),
    ]
    answers = inquirer.prompt(questions)

    inject.get_session_captcha()
    time.sleep(1)

    if inject.post_solve_captcha(captcha_result=inject.captcha_solver()):

        print("\n[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTGREEN_EX + "Success Solve Captcha" + "\n")

        if answers['type'] == 'Views':

            while True:
                inject_views = inject.send_views(
                    url_video=url_video
                )

                if inject_views:

                    if inject_views['message'] == "Please try again later":
                        print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_views['message'])
                        exit()

                    elif inject_views['message'] == 'Another State':
                        print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTGREEN_EX + "Current Views: " +
                              inject_views['data'], end="\n\n")


                    elif inject_views['message'] == "Successfully views sent.":
                        print("[ " + str(
                            datetime.datetime.now()) + " ] " + Fore.LIGHTGREEN_EX + inject_views[
                                  'message'] + " to " + Fore.LIGHTYELLOW_EX + "" + url_video,
                              end="\n\n")

                    elif inject_views['message'] == "Session Expired. Please Re Login!":
                        print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_views['message'])
                        exit()

                    # elif inject_views['message'] == "Please try again later. Server too busy.":
                    #     print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_views['message'])
                    #     exit()

                    else:
                        for i in range(int(inject_views['message']), 0, -1):
                            print("[ " + str(
                                datetime.datetime.now()) + " ] " + Fore.LIGHTYELLOW_EX + "Please wait " + str(
                                i) + " seconds to send views again.", end="\r")
                            time.sleep(1)

                    time.sleep(random.randint(1, 5))

                else:
                    pass

        elif answers['type'] == 'Shares':

            while True:
                inject_shares = inject.send_shares(
                    url_video=url_video
                )

                if inject_shares:

                    if inject_shares['message'] == "Please try again later":
                        print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_shares['message'])
                        exit()

                    elif inject_shares['message'] == 'Another State':
                        print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTGREEN_EX + "Current Shares : " +
                              inject_shares['data'], end="\n\n")


                    elif inject_shares['message'] == "Shares successfully sent.":
                        print("[ " + str(
                            datetime.datetime.now()) + " ] " + Fore.LIGHTGREEN_EX + inject_shares[
                                  'message'] + " to " + Fore.LIGHTYELLOW_EX + "" + url_video,
                              end="\n\n")

                    elif inject_shares['message'] == "Session Expired. Please Re Login!":
                        print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_shares['message'])
                        exit()

                    # elif inject_shares['message'] == "Please try again later. Server too busy.":
                    #     print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_shares['message'])
                    #     exit()

                    else:
                        for i in range(int(inject_shares['message']), 0, -1):
                            print("[ " + str(
                                datetime.datetime.now()) + " ] " + Fore.LIGHTYELLOW_EX + "Please wait " + str(
                                i) + " seconds to send Shares again.", end="\r")
                            time.sleep(1)

                    time.sleep(random.randint(1, 5))

                else:
                    pass

        elif answers['type'] == 'Favorites':

            while True:
                inject_favorites = inject.send_favorites(
                    url_video=url_video
                )

                if inject_favorites:

                    if inject_favorites['message'] == "Please try again later":
                        print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_favorites[
                            'message'])
                        exit()

                    elif inject_favorites['message'] == 'Another State':
                        print(
                            "[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTGREEN_EX + "Current Favorites : " +
                            inject_favorites['data'], end="\n\n")

                    elif inject_favorites['message'] == "Favorites successfully sent.":
                        print("[ " + str(
                            datetime.datetime.now()) + " ] " + Fore.LIGHTGREEN_EX + inject_favorites[
                                  'message'] + " to " + Fore.LIGHTYELLOW_EX + "" + url_video,
                              end="\n\n")

                    elif inject_favorites['message'] == "Session Expired. Please Re Login!":
                        print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_favorites[
                            'message'])
                        exit()

                    # elif inject_favorites['message'] == "Please try again later. Server too busy.":
                    #     print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_favorites[
                    #         'message'])
                    #     exit()

                    else:
                        for i in range(int(inject_favorites['message']), 0, -1):
                            print("[ " + str(
                                datetime.datetime.now()) + " ] " + Fore.LIGHTYELLOW_EX + "Please wait " + str(
                                i) + " seconds to send Favorites again.", end="\r")
                            time.sleep(1)

                    time.sleep(random.randint(1, 5))

                else:
                    pass

    else:
        print(Fore.RED + "Failed to solve captcha.")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "Exit")
        exit()
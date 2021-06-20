try:
    from simple_colors import *
    from vaporwavely import vaporize
    from pySpaceX import Space
except ImportError:
    import os
    print("Imports failed! Attempting to install imports!")
    os.sys("pip3 install simple_colors")
    os.sys("pip3 install vaporwavely")
    os.sys("pip3 install pySpaceX")
    from simple_colors import *
    from vaporwavely import vaporize
    from pySpaceX import Space


class SpaceX:

    def __init__(self):
        self.api = Space()

    def get_dash(self):
        dash = magenta("=" * 50)
        return dash

    def footer(self):
        dash = cyan('-' * 20)
        return dash

    def header(self):
        try:
            print(magenta(self.get_dash()))
            print(vaporize("SpaceX API Tool"))
            print(magenta(self.get_dash()))
        except Exception as e:
            print("SpaceX API Tool")

    def user_input(self):
        input_list = []
        print(green(
            "Search:\n"
            "1. 'crew' to get information of SpaceX's staff\n"
            "2. 'rockets' to get information of SpaceX's rockets\n"
            "3. 'launches' to get information of SpaceX's launches\n"
            "4. Anything else runs all :)\n")

        )
        user_input = input("Enter: ")
        if 'crew' in user_input.lower():
            input_list.append("crew")
        elif 'rockets' in user_input.lower():
            input_list.append("rockets")
        elif 'launches' in user_input.lower():
            input_list.append("launches")
        else:
            input_list = ['crew', 'rockets', 'launches']
        return input_list

    def controller(self):
        self.header()
        self.spaceX()

    def launches_info(self):
        print(cyan("Launches Information"))
        print(self.get_dash())
        launches = self.api.get_launches().launches()
        for launch in launches:

            print("Rocket: " + str(self.rocket_id_to_name(launch["rocket"])['name']))
            print("Rocket: " + str(self.crew_id_to_name(launch["crew"])))
            if launch["success"]:
                print(green("Success: " + str(launch["success"])))
            else:
                print(red("Success: " + str(launch["success"])))
            print("Launch details: " + str(launch['details']))
            print(self.footer())

    def rocket_id_to_name(self, id):
        return self.api.get_rockets().one_rocket(id)

    def crew_id_to_name(self, id):
        try:
            return self.api.get_crew().one_crew_member(id)['name']
        except Exception as no_crew_found:
            return red("No crew found")

    def rockets_info(self):
        print(cyan("Rocket Information"))
        print(self.get_dash())
        rockets = self.api.get_rockets()
        for rocket in rockets.rockets():
            print(cyan(rocket['name'] + ':'))
            print(rocket['description'])
            print(f'Total cost: {red(rocket["cost_per_launch"])} dollars.')
            print(self.footer())

    def starlink_info(self):
        print(cyan("Starlink Information"))
        print(self.get_dash())
        stars = self.api.get_starlink()
        for star in stars.starlink():
            print(star['spaceTrack'])

    def get_crew(self):
        print(cyan("Crew Information"))
        print(self.get_dash())
        for crew in self.api.get_crew().members():
            print("Staff Memeber: " + crew['name'])
            print("Agency: " + crew['agency'])
            print("Image: " + crew['image'])
            print(self.footer())

    def spaceX(self):
        inputs = self.user_input()
        if 'crew' in inputs:
            self.get_crew()
        if 'rockets' in inputs:
            self.rockets_info()
        if 'launches' in inputs:
            self.launches_info()


if __name__ == '__main__':
    space_obj = SpaceX()
    space_obj.controller()

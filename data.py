from university import *


class Data:
    ROOMS = [       ["A1", 25],
                    ["B2", 26],
                    ["C3", 30],
                    ["D4", 30],
                    ["E5", 25],
                    ["F6", 26],
                    ["G7", 30],
                    ["H8", 30],
                    ["I9", 15],
                    ["J10", 30],
                    ["K11", 20],
                    ["L12", 25],
                    ["M13", 26],
                    ["N14", 20],
                    ["O15", 30]


         ]
    MEETING_TIMES = [["09:00 - 11:00MONDAY"],
                     ["11:00 - 13:00MONDAY"],
                     ["13:00 - 15:00MONDAY"],
                     ["15:00 - 17:00MONDAY"],
                     ["17:00 - 19:00MONDAY"],
                     ["19:00 - 21:00MONDAY"],

                     ["09:00 - 11:00TUESDAY"],
                     ["11:00 - 13:00TUESDAY"],
                     ["13:00 - 15:00TUESDAY"],
                     ["15:00 - 17:00TUESDAY"],
                     ["17:00 - 19:00TUESDAY"],
                     ["19:00 - 21:00TUESDAY"],

                     ["09:00 - 11:00WEDNESDAY"],
                     ["11:00 - 13:00WEDNESDAY"],
                     ["13:00 - 15:00WEDNESDAY"],
                     ["15:00 - 17:00WEDNESDAY"],
                     ["17:00 - 19:00WEDNESDAY"],
                     ["19:00 - 21:00WEDNESDAY"],

                     ["09:00 - 11:00THURSDAY"],
                     ["11:00 - 13:00THURSDAY"],
                     ["13:00 - 15:00THURSDAY"],
                     ["15:00 - 17:00THURSDAY"],
                     ["17:00 - 19:00THURSDAY"],
                     ["19:00 - 21:00THURSDAY"],

                     ["09:00 - 11:00FRIDAY"],
                     ["11:00 - 13:00FRIDAY"],
                     ["13:00 - 15:00FRIDAY"],
                     ["15:00 - 17:00FRIDAY"],
                     ["17:00 - 19:00FRIDAY"],
                     ["19:00 - 21:00FRIDAY"]
                     ]
    INSTRUCTORS = [["James Web"],
                   ["Mike Brown"],
                   ["Steve Day"],
                   ["George Miller"],
                   ["Lily Johns"],
                   ["Jannifer Dickens"],
                   ["Jane Doe"],
                   ["Andrew Lively"],
                   ["John Drake"],
                   ["Mila Kasper"],
                   ["Katherine Balvin"],
                   ["Stamatia Papa"],
                   ["Austin Day"],
                   ["Helena Kosta"],
                   ["Eirini Best"]
                  ]

    def __init__(self):
        self._rooms = []
        self._meetingTimes = []
        self._instructors = []
        for i in range(0, len(self.ROOMS)):
            self._rooms.append(Audience(self.ROOMS[i][0], self.ROOMS[i][1]))
        for i in range(0, len(self.MEETING_TIMES)):
            self._meetingTimes.append(LessonTime(self.MEETING_TIMES[i][0]))
        for i in range(0, len(self.INSTRUCTORS)):
            self._instructors.append(Teacher(self.INSTRUCTORS[i][0]))

        subject1 = Subject("Algorithms", [self._instructors[0],self._instructors[7],self._instructors[3]], 30)
        subject2 = Subject("Database", [self._instructors[4],self._instructors[10],self._instructors[8]], 19)
        subject3 = Subject("Cloud Computing", [ self._instructors[2],self._instructors[11],self._instructors[3]], 30)
        subject4 = Subject("Web Development", [self._instructors[4] ,self._instructors[0],self._instructors[10]], 30)
        subject5 = Subject("Application Engineering", [self._instructors[12],self._instructors[11],self._instructors[8]], 25)
        subject6 = Subject("Data Science", [ self._instructors[10],self._instructors[11],self._instructors[14]], 25)
        subject7 = Subject("Business Intelligence", [self._instructors[10],self._instructors[2],self._instructors[8]], 30)
        subject8 = Subject("JAVA", [ self._instructors[4],self._instructors[0],self._instructors[14]], 22)
        subject9 = Subject("Python", [ self._instructors[0],self._instructors[11],self._instructors[8]], 26)
        subject10 = Subject("C++", [self._instructors[4],self._instructors[6],self._instructors[14]], 30)
        subject11 = Subject("Mathematics 2", [self._instructors[2],self._instructors[5],self._instructors[7]], 30)
        subject12 = Subject("Matlab", [self._instructors[8],self._instructors[2],self._instructors[11]], 26)
        subject13 = Subject("SQL", [self._instructors[10],self._instructors[8],self._instructors[5]], 15)
        subject14 = Subject("Javascript", [ self._instructors[8],self._instructors[11],self._instructors[5]], 20)
        subject15 = Subject("HTML", [self._instructors[0],self._instructors[8],self._instructors[4]], 30)
        subject16 = Subject("Mathematics 3", [self._instructors[2],self._instructors[5], self._instructors[7]], 30)
        subject17 = Subject("Matlab 2 (Epilogis)", [self._instructors[5], self._instructors[10],self._instructors[11]], 26)
        subject18 = Subject("SQL 2", [self._instructors[0], self._instructors[11],self._instructors[10]], 15)
        subject19 = Subject("Javascript 2 (Epilogis)", [self._instructors[11],self._instructors[0],self._instructors[4]], 30)
        subject20 = Subject("HTML 2 (Epilogis)", [self._instructors[0], self._instructors[10],self._instructors[4]], 30)

        subject21 = Subject("Algorithms 2", [self._instructors[14], self._instructors[4],self._instructors[6]], 30)
        subject22 = Subject("Database 2 (Epilogis)", [self._instructors[11],self._instructors[7],self._instructors[6]], 30)
        subject23 = Subject("Cloud Computing 2 (Epilogis) ", [self._instructors[10], self._instructors[11],self._instructors[7]], 20)
        subject24 = Subject("Web Development 2", [self._instructors[7],self._instructors[8],self._instructors[14]], 30)
        subject25 = Subject("Application Engineering 2 (Epilogis)", [self._instructors[4], self._instructors[14],self._instructors[7]], 30)

        subject26 = Subject("Python Practice",[ self._instructors[0],self._instructors[11],self._instructors[8]], 26)
        subject27 = Subject("C++ Practice", [self._instructors[4],self._instructors[6],self._instructors[14]], 30)
        subject28 = Subject("SQL Practice", [self._instructors[10],self._instructors[8],self._instructors[5]], 15)

        subject29 = Subject("Matlab 2 (Epilogis) Practice", [self._instructors[5], self._instructors[10],self._instructors[11]], 26)
        subject30 = Subject("SQL 2 Practice", [self._instructors[0], self._instructors[11],self._instructors[10]], 15)
        subject31 = Subject("Javascript 2 (Epilogis) Practice", [self._instructors[11],self._instructors[0],self._instructors[4]], 30)
        subject32 = Subject("HTML 2 (Epilogis) Practice", [self._instructors[0], self._instructors[10],self._instructors[4]], 30)

        subject33 = Subject("JAVA Practice", [ self._instructors[4],self._instructors[0],self._instructors[14]], 22)
        subject34 = Subject("Matlab Practice", [self._instructors[8],self._instructors[2],self._instructors[11]], 26)
        subject35 = Subject("Javascript Practice", [ self._instructors[8],self._instructors[11],self._instructors[5]], 20)
        subject36 = Subject("HTML Practice", [self._instructors[0],self._instructors[8],self._instructors[4]], 30)

        subject37 = Subject("Database 2 (Epilogis) Practice", [self._instructors[11],self._instructors[7],self._instructors[6]], 30)
        subject38 = Subject("Web Development 2 Practice", [self._instructors[7],self._instructors[8],self._instructors[14]], 30)
        subject39 = Subject("Application Engineering 2 (Epilogis)  Practice", [self._instructors[4], self._instructors[14],self._instructors[7]], 30)
        subject40 = Subject("Algorithms 2 Practice", [self._instructors[14], self._instructors[4], self._instructors[6]], 30)
        subject41 = Subject("Cloud Computing 2 (Epilogis)  Practice", [self._instructors[10], self._instructors[11],self._instructors[7]], 20)
        subject42 = Subject("Database  Practice", [self._instructors[4],self._instructors[10],self._instructors[8]], 19)

        subject43 = Subject("Algorithms Practice", [self._instructors[0],self._instructors[7],self._instructors[3]], 30)
        subject44 = Subject("Cloud Computing Practice", [self._instructors[11],self._instructors[2],self._instructors[3]], 30)
        subject45 = Subject("Application Engineering Practice", [self._instructors[12],self._instructors[11],self._instructors[8]], 25)
        subject46 = Subject("Web Development Practice", [self._instructors[4] ,self._instructors[0],self._instructors[10]], 30)
        subject47 = Subject("Data Science Practice", [self._instructors[10],self._instructors[11],self._instructors[14]], 25)
        subject48 = Subject("Business Intelligence Practice", [self._instructors[10],self._instructors[2],self._instructors[8]], 30)
        subject49 = Subject("Mathematics 2 Practice", [self._instructors[10],self._instructors[11],self._instructors[0]], 30)

        subject50 = Subject("Algorithms 3", [self._instructors[1], self._instructors[6], self._instructors[2]], 30)
        subject51 = Subject("Database 3 (Epilogis)", [self._instructors[2], self._instructors[1], self._instructors[7]],30)
        subject52 = Subject("Cloud Computing 3 (Epilogis)", [self._instructors[0], self._instructors[2], self._instructors[7]], 20)
        subject53 = Subject("Web Development 3",[self._instructors[1], self._instructors[10], self._instructors[2]], 30)
        subject54 = Subject("Application Engineering 3 (Epilogis)",[self._instructors[11], self._instructors[0], self._instructors[7]], 30)
        subject55 = Subject("Mathematics 3 Practice", [self._instructors[4], self._instructors[11], self._instructors[5]], 30)

        subject56 = Subject("Web Development 3 Practice",[self._instructors[1], self._instructors[10], self._instructors[2]],30)
        subject58 = Subject("Application Engineering 3 (Epilogis) Practice",[self._instructors[11], self._instructors[0], self._instructors[7]], 30)
        subject57 = Subject("Cloud Computing 3 (Epilogis) Practice", [self._instructors[0], self._instructors[2], self._instructors[7]], 20)
        subject59 = Subject("Database 3 (Epilogis) Practice",[self._instructors[2], self._instructors[1], self._instructors[7]], 30)
        subject60 = Subject("Algorithms 3 Practice", [self._instructors[1], self._instructors[6], self._instructors[2]], 30)

        self._subjects = [subject1, subject2, subject3, subject4, subject5, subject6, subject7, subject8,subject9,subject10,subject11,subject12,subject13,subject14,subject15,subject16,subject17,subject18,subject19,subject20,subject21,subject22,subject23,subject24,subject25,subject26,subject27,subject28,subject29,subject30,subject31,subject32,subject33,subject34,subject35,subject36,subject37,subject38,subject39,subject40,subject41,subject42,subject43,subject44,subject45,subject46,subject47,subject48,subject49,subject50,subject51,subject52,subject53,subject54,subject55,subject56,subject57,subject58,subject59,subject60]

        spec1 = Speciality("1st Year", [subject1,subject5,subject7,subject12,subject34,subject34])
        spec2 = Speciality("2nd Year", [subject9,subject26,subject26,subject21,subject3,subject36,subject36,subject15])
        spec3 = Speciality("3rd Year", [subject11,subject50,subject13,subject28,subject28,subject24])
        spec4 = Speciality("4th Year", [subject16,subject14,subject35,subject35,subject17,subject20,subject32])
        spec5 = Speciality("5th Year", [subject19,subject8,subject33,subject33,subject10,subject27,subject27,subject18])
        self._specs = [spec1, spec2, spec3,spec4,spec5]

        self._numberOfClasses = 0
        for i in range(0, len(self._specs)):
            self._numberOfClasses += len(self._specs[i]._subjects)

def admission_chatbot():
    print("Welcome to Adhiyamaan College Admission Chatbot!")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Chatbot: Thanks for reaching out! Have a great day!")
            break
        elif "courses" in user_input or "programs" in user_input:
            print("Chatbot: We offer B.Tech, M.Tech, MBA, and Diploma programs.")
        elif "branches" in user_input or "departments" in user_input:
            print("Chatbot: CSE, ECE, EEE, Mechanical, Civil, IT, AI & DS, and more.")
        elif "fees" in user_input:
            print("Chatbot: Fees vary by course. Visit our website for details.")
        elif "admission process" in user_input or "how to apply" in user_input:
            print("Chatbot: Apply online, submit documents, and attend entrance test if required.")
        elif "scholarship" in user_input:
            print("Chatbot: Merit and need-based scholarships available.")
        elif "placements" in user_input:
            print("Chatbot: Top recruiters include TCS, Infosys, Amazon, and L&T.")
        elif "hostel" in user_input or "accommodation" in user_input:
            print("Chatbot: Separate hostels for boys & girls with mess and WiFi.")
        elif "facilities" in user_input:
            print("Chatbot: Library, labs, sports, hostels, and transport available.")
        elif "duration" in user_input:
            print("Chatbot: B.Tech - 4 years, M.Tech - 2 years, MBA - 2 years.")
        elif "faculty" in user_input:
            print("Chatbot: Experienced faculty with PhDs and industry experience.")
        elif "extracurricular" in user_input:
            print("Chatbot: Clubs, sports, fests, and workshops for student growth.")
        elif "internships" in user_input:
            print("Chatbot: Internship opportunities in top MNCs & startups.")
        elif "contact" in user_input:
            print("Chatbot: Call +91-9876543210 or email admissions@adhiyamaan.ac.in.")
        else:
            print("Chatbot: Sorry, I didn't get that. Ask about courses, fees, admissions, or placements.")


admission_chatbot()
from django.shortcuts import render

def admin_dashboard(request):
    # Fetch the required data for the dashboard, such as total students, recent activity, etc.
    context = {
        'total_students': 100,  # Example data; replace with actual data
        'new_students': 10,
        'unread_messages': 5,
        'recent_students': [
            {'first_name': 'John', 'last_name': 'Doe', 'student_class': 'A1', 'gender': 'Male'},
            # Add other students as required
        ],
    }
    return render(request, 'admin/admin-dashboard.html', context)

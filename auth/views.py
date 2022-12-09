from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from leads.models import User
from django.views.decorators.csrf import ensure_csrf_cookie , csrf_protect  
from django.utils.decorators import method_decorator



@method_decorator(csrf_protect , name='dispatch')
class SignUpView(APIView):
    
    permission_classes = (permissions.AllowAny,)
    
    
    def post(self , request , format = None):
        
        data = self.request.data
        
        email = data['email']
        username = data['username']
        first_name = data['first_name']
        last_name = data['last_name']
        password = data['password']
        confirm_pass = data['confirm_password']
        
        if password == confirm_pass:
            if User.objects.filter(username=username).exists():
                return Response({"error": "Username already taken"}) 
            if User.objects.filter(email=email).exists():
                return Response({"error": "Email already exists"})
            else:
                if len(password)<6:
                    return Response({"error":"Password must be atleast 6 characters"})
                else:
                    user = User.objects.create_user(email=email,username=username,first_name=first_name,last_name=last_name,password=password)
                    user.save()
                    return Response({"success": "User created successfully"})
        else:
            return Response({"error": "Password doesn't match"})
    

@method_decorator(ensure_csrf_cookie , name='dispatch')
class GetCSRFToken(APIView):
    
    permission_classes = (permissions.AllowAny,)
    
    def get(self,request,format=None):
        return Response({'success': 'csrf_cookie_set'})
        
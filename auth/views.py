from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.models import auth
from leads.models import User
from django.views.decorators.csrf import ensure_csrf_cookie , csrf_protect  
from django.utils.decorators import method_decorator



@method_decorator(csrf_protect , name='dispatch')
class CheckAuthenticateView(APIView):
    
    def get(self , request , format=None):
        
        IsAuthenticated = User.is_authenticated
        
        try:
            if IsAuthenticated:
                
                return Response ({'IsAutheticated': 'successs'})
            
            else:
                
                return Response ({'IsAutheticated': 'error'})
        except:
            
            return Response ({'error': 'something went wrong when checking authetication status'})



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
        
        try:
            if password == confirm_pass:
                
                if User.objects.filter(email=email).exists():
                    return Response({"error": "Email already exists"})
                else:
                    if len(password)<6:
                        return Response({"error":"Password must be atleast 6 characters"})
                    
                    elif User.objects.filter(username=username).exists():
                        return Response({'error':'username already exists'})
                    
                    else:
                        user = User.objects.create_user(email=email,username=username,first_name=first_name,last_name=last_name,password=password)
                        user.save()
                        return Response({"success": "User created successfully"})
                          
            return Response({"error": "Password doesn't match"})
        except:
                return Response({'error':'something went wrong'})
        
        

@method_decorator(csrf_protect , name='dispatch')  
class LoginView(APIView):
    
    permission_classes = (permissions.AllowAny,)
    
    def post(self,request,format=None):
        
        data = self.request.data
        
        email = data['email']
        password = data['password']
        
        try:
            user = auth.authenticate(email=email , password=password)
            
            if user is not None:
                auth.login(request,user)
                return Response({'success': 'user authenticated'})
            else:
                return Response({'error':'invalid credentials'})
        except:
            return Response({'error':'something went wrong while loggin in'})
        
        
class LogoutView(APIView):
    
    def post(self,request,format = None):
        try:
            auth.logout(request)
            return Response({'success': 'successfully Log out'})
        except:
            
            return Response({'error': 'something went wrong'})
    
    
    
    
@method_decorator(ensure_csrf_cookie , name='dispatch')
class GetCSRFToken(APIView):
    
    permission_classes = (permissions.AllowAny,)
    
    def get(self,request,format=None):
        return Response({'success': 'csrf_cookie_set'})
        
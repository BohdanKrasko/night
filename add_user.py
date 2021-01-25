from ansible.module_utils.basic import *
import os
import sys
import django

def add_user_present(data):

    sys.path.append(data['path'])
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', data['project_name'] + '.settings')

    django.setup()
    
    from django.contrib.auth.models import User
    
    username = data['username']
    email = data['email']
    password = data['password']

    if User.objects.filter(username=username).exists():
        return False, False, {'response': 'User alredy exists'}
    else:
        User.objects.create_superuser(username, email, password)
        return False, True, {'response': 'User {} added'.format(username)}

    meta = {'status': True, 'response': 'Error'}
    return True, True,  meta

def main():
    fields = {
            'project_name': {'required': True, 'type': 'str'},
            'path': {'required': True, 'type': 'str'},
            'username': {'required': True, 'type': 'str'},
            'email': {'required': True, 'type': 'str'},
            'password': {'required': True, 'type': 'str'},
            'state': {
                    'default': 'present',
                    'choices': ['present'],
                    'type': 'str'
                },
            }
    choice_map = {
            'present': add_user_present,
            }
    
    module = AnsibleModule(argument_spec=fields)
    is_error, has_changed, result = choice_map.get(
            module.params['state'])(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg='Error add user', meta=result)

if __name__ == '__main__':
    main()

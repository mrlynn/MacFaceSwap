# Path: src/core/premium_manager.py
import keyring
import json
from datetime import datetime, timedelta

class PremiumManager:
    def __init__(self):
        self.keyring_service = "mac_face_swap"
        self.keyring_username = "premium_status"
        
    def is_premium(self) -> bool:
        """Check if user has premium status"""
        try:
            status = keyring.get_password(self.keyring_service, self.keyring_username)
            if not status:
                return False
                
            status_data = json.loads(status)
            if status_data.get('lifetime_premium'):
                return True
                
            # Check trial period
            trial_start = datetime.fromisoformat(status_data.get('trial_start', '2000-01-01'))
            trial_days = status_data.get('trial_days', 0)
            
            if datetime.now() - trial_start < timedelta(days=trial_days):
                return True
                
            return False
            
        except Exception:
            return False
            
    def activate_premium(self, is_lifetime: bool = True):
        """Activate premium features"""
        status = {
            'lifetime_premium': is_lifetime,
            'activation_date': datetime.now().isoformat()
        }
        keyring.set_password(
            self.keyring_service,
            self.keyring_username,
            json.dumps(status)
        )
        
    def start_trial(self, days: int = 14):
        """Start free trial period"""
        status = {
            'lifetime_premium': False,
            'trial_start': datetime.now().isoformat(),
            'trial_days': days
        }
        keyring.set_password(
            self.keyring_service,
            self.keyring_username,
            json.dumps(status)
        )
        
    def clear_status(self):
        """Clear all premium status (for testing)"""
        try:
            keyring.delete_password(self.keyring_service, self.keyring_username)
        except Exception:
            pass
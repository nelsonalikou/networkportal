export function isAuthenticated(): boolean {
   return !!localStorage.getItem('access_token');
}

export function logout() {
   localStorage.removeItem('access_token');
   window.location.href = '/login';
}

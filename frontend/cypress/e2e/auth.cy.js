describe('Flujo de Autenticación', () => {
  it('debe redirigir al login si no hay token', () => {
    cy.visit('/dashboard');
    cy.url().should('include', '/login');
  });

  it('debe permitir el acceso con credenciales correctas', () => {
    cy.intercept('POST', '/api/token/', {
      statusCode: 200,
      body: { access: 'fake-token', refresh: 'fake-refresh' }
    }).as('loginRequest');

    cy.visit('/login');
    cy.get('input[name="username"]').type('entrenador_pro');
    cy.get('input[name="password"]').type('password123');
    cy.get('button[type="submit"]').click();

    cy.wait('@loginRequest');
    cy.url().should('include', '/dashboard');
    cy.contains('Bienvenido').should('be.visible');
  });
});
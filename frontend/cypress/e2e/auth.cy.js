describe('Flujo de Autenticación', () => {
  it('debe redirigir al login si no hay token', () => {
    cy.visit('/');
    cy.url().should('include', '/login');
  });

  it('debe permitir el acceso con credenciales correctas', () => {
    cy.intercept('POST', '**/api/auth/login/', {
      statusCode: 200,
      body: { 
        access: 'fake-access-token', 
        refresh: 'fake-refresh-token' 
      }
    }).as('loginRequest');

    cy.intercept('GET', '**/api/auth/user/', {
      statusCode: 200,
      body: { is_staff: true }
    }).as('userRequest');

    cy.visit('/login');

    cy.get('input[name="username"]').type('entrenador_pro');
    cy.get('input[name="password"]').type('password123');
    cy.get('button[type="submit"]').click();

    cy.wait('@loginRequest');
    cy.wait('@userRequest');
    
    cy.url().should('eq', Cypress.config().baseUrl + '/'); 
  });
});
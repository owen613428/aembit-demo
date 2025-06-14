# Aembit Secrets Management Demo

[![Security: Demo Only](https://img.shields.io/badge/Security-Demo%20Only-red)](SECURITY_DISCLAIMER.md)
[![Aembit: Integrated](https://img.shields.io/badge/Aembit-Integrated-green)](https://aembit.io)

## 🎯 Purpose

This repository demonstrates the security transformation possible with Aembit - from traditional CI/CD pipelines full of secrets to zero-secrets deployment with workload identity.

## ⚠️ Important: Demo Environment Only

**This repository contains intentionally vulnerable code for demonstration purposes.**
- All credentials are fake and for demo only
- Vulnerable applications expose secrets intentionally  
- This demonstrates what NOT to do vs. secure practices
- [Read full security disclaimer](SECURITY_DISCLAIMER.md)

## 🏗️ What's Demonstrated

### Vulnerable CI/CD (Traditional Approach)
- ❌ Secrets stored in GitHub Actions secrets
- ❌ Hardcoded credentials in application code
- ❌ Environment variables with sensitive data
- ❌ Secrets visible in CI/CD logs
- ❌ Manual secret rotation required

### Secure CI/CD (Aembit Approach)  
- ✅ Zero secrets in CI/CD pipeline
- ✅ GitHub OIDC workload identity
- ✅ Dynamic credential injection
- ✅ Automatic credential rotation
- ✅ Complete audit trail

## 🚀 Live Demo Workflows

### 1. Vulnerable Deployment
- **Workflow**: `.github/workflows/vulnerable-deploy.yml`
- **Purpose**: Shows traditional secrets management risks
- **Result**: Functional but insecure deployment

### 2. Secure Deployment  
- **Workflow**: `.github/workflows/secure-deploy.yml`
- **Purpose**: Demonstrates Aembit zero-secrets approach
- **Result**: Same functionality, zero secrets

### 3. Security Comparison
- **Workflow**: `.github/workflows/security-comparison.yml`
- **Purpose**: Automated analysis of both approaches
- **Result**: Detailed security assessment report

## 📱 Sample Applications

### E-commerce Web App
- **Vulnerable**: `vulnerable-webapp/` - Hardcoded database credentials
- **Secure**: `secure-webapp/` - Aembit SDK integration
- **Features**: Product catalog, simulated database, API integrations

### Inventory API
- **Vulnerable**: `vulnerable-api/` - API keys in source code  
- **Secure**: `secure-api/` - Workload identity authentication
- **Features**: REST API, simulated data, external service integration

## 🎬 Running the Demo

### Prerequisites
- GitHub account with Actions enabled
- Aembit tenant (for secure workflows)
- Basic understanding of CI/CD concepts

### Quick Start
1. **Fork this repository** to your GitHub account
2. **Configure GitHub Actions secrets** (for vulnerable demo):
   - `DATABASE_URL`: `postgresql://demo:fake123@localhost:5432/demo`
   - `EXTERNAL_API_KEY`: `sk-demo-fake-api-key-12345`  
   - `JWT_SECRET`: `demo-jwt-secret-not-real`
3. **Run workflows**:
   - Go to Actions tab
   - Run "🚨 Vulnerable Deployment" workflow
   - Run "✅ Secure Deployment" workflow
   - Run "🔍 Security Comparison" workflow

### For Aembit Integration
- Set up GitHub Actions trust provider in Aembit
- Configure workload identities for CI/CD pipeline
- See [Aembit configuration guide](docs/aembit-setup.md)

## 📊 Demo Results

After running the workflows, you'll see:

1. **Vulnerable deployment logs** showing secrets in CI/CD output
2. **Secure deployment logs** with zero secrets exposed
3. **Security comparison report** highlighting the transformation
4. **Downloadable artifacts** with detailed analysis

## 🔗 Resources

- [Aembit Documentation](https://docs.aembit.io)
- [GitHub Actions OIDC](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
- [Security Best Practices](docs/security-best-practices.md)



---

## 🔒 Security Transformation Summary

| Aspect | Before Aembit | After Aembit |
|--------|---------------|--------------|
| Secrets in Code | ❌ Hardcoded everywhere | ✅ Zero secrets |
| CI/CD Security | ❌ Secrets in logs | ✅ OIDC tokens only |
| Developer Access | ❌ All secrets visible | ✅ No secret access |
| Rotation | ❌ Manual process | ✅ Automatic |
| Audit Trail | ❌ Limited visibility | ✅ Complete audit |
| Compliance | ❌ Complex to prove | ✅ Automated reporting |

**The result**: Same functionality, dramatically improved security posture.

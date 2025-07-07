# 🎯 LiveKit Voice Agent with SIP Telephony Integration

## 🎯 Project Overview

This project implements a sophisticated **Voice AI Agent** that can handle both web-based voice interactions and **real phone calls** through SIP (Session Initiation Protocol) integration. The agent uses Azure Cognitive Services for speech recognition and text-to-speech, Azure OpenAI for intelligent conversations, and LiveKit for real-time communication infrastructure.

### ✨ Key Features

- **🎙️ Voice AI Agent**: Natural conversation with speech recognition and synthesis
- **📞 Phone Call Integration**: Accept and make real phone calls via SIP trunks
- **🤖 Azure OpenAI Integration**: Intelligent responses powered by GPT models
- **🔊 Azure Speech Services**: High-quality speech-to-text and text-to-speech
- **🐳 Docker Infrastructure**: Complete containerized setup with LiveKit server
- **📱 Twilio Integration**: Production-ready phone number management
- **💬 Conversation Export**: Automatic conversation logging and export
- **🔧 Cross-Platform Support**: Windows, Mac, and Linux deployment
- **⚡ Intelligent Startup**: Smart/Simple/Legacy modes with health checks
- **🎯 Unified SIP Management**: Consolidated trunk management system
- **🗣️ Dynamic AI Personalities**: Configure agents via YAML files instead of code
- **🧩 Modular & Clean Architecture**: Easy to maintain, extend, and understand

---

## 🚀 Quick Start (Multiple Options)

### **🎯 Option 1: Smart Mode (Recommended)**
```bash
# Intelligent startup with health checks
python start_optimized.py

# Alternative: Doppelklick functionality
# Windows: start_scripts/start_docker.bat (choose option 1)
# Linux/Mac: start_scripts/start_docker.sh (choose option 1)
```

### **⚡ Option 2: Simple Mode (Fast)**
```bash
# Quick startup without health checks
python start_optimized.py --simple

# Via doppelklick: Choose option 2 in wrapper scripts
```

### **🔧 Option 3: Legacy Mode (Compatible)**
```bash
# Pure Docker Compose (traditional method)
docker-compose up -d --build

# Via doppelklick: Choose option 3 in wrapper scripts
```

### **📋 Getting Started Steps:**

1. **Configure Credentials**: Copy `.env.example` to `.env` and add your API keys
   ```bash
   cp .env.example .env
   ```

2. **Start the System**: Use intelligent startup scripts (Python 3.11+ required)
   ```bash
   # For Windows
   .\start_scripts\start_docker.bat
   
   # For macOS / Linux
   chmod +x ./start_scripts/start_docker.sh
   ./start_scripts/start_docker.sh
   ```

3. **Make a Test Call**: Use the REST API with an API key to place an outbound call
   ```bash
   curl -X POST "http://localhost:8000/api/outbound-call" \
        -H "Content-Type: application/json" \
        -H "X-API-Key: <your-key>" \
        -d '{"to_number": "+15551234567"}'
   ```
4. **Test the Voice Pipeline**: Send audio to the new pipeline endpoint
   ```bash
   curl -X POST "http://localhost:8000/api/voice-pipeline" \
        -H "X-API-Key: <your-key>" \
        -F "file=@sample.wav"
   ```
5. **Trigger a Webhook**: POST an event to the webhook endpoint
   ```bash
   curl -X POST "http://localhost:8000/api/webhook" \
        -H "X-API-Key: <your-key>" \
        -H "Content-Type: application/json" \
        -d '{"type": "ping"}'
   ```

6. **Generate Tasks**: Use the Taskmaster CLI to parse the PRD
   ```bash
   python scripts/task_master.py initialize-project
   python scripts/task_master.py parse-prd VAPI_HOMEMADE_PRD.md --limit 5
   python scripts/task_master.py next-task
   ```
   The tasks are saved to `tasks.json` in the project root so they can be tracked
   with version control.

---

## 🏗️ Architecture Overview

```
┌─────────────────┐                              ┌──────────────────┐
│   API Clients   │          (HTTPS)             │    Phone Call    │
│  (N8N, curl)    │----------------------------->│    (via Twilio)    │
└─────────────────┘                              └──────────────────┘
         |                                                 | (SIP)
         v                                                 v
┌────────────────┐                              ┌────────────────┐
│   API Server   │                              │   SIP Server   │
│    (Docker)    │                              │    (Docker)    │
└────────┬───────┘                              └────────┬───────┘
         | (Adds Job)                                      | (RTC)
         v                                                 v
┌────────────────┐                              ┌────────────────┐
│      Redis     │<--------(Uses for Queue)-----│  LiveKit Server│
│ (Queue/Broker) │                              │(RTC Signaling) │
└────────┬───────┘                              └────────┬───────┘
         | (Pulls Job)                                     | (Connects)
         |                                                 |
         └--------------------┬------------------------------┘
                              |
                              v
                     ┌────────────────┐
                     │  Voice Agent   │
                     │ (Worker Docker)│
                     └────────┬───────┘
                              | (API Calls)
                              v
                     ┌────────────────┐
                     │ Azure Services │
                     │(Speech, OpenAI)│
                     └────────────────┘
```

---

## 📁 Updated Project Structure

```
voice-agent-project/
├── 📄 config.py                      # Configuration management class
├── 📄 docker-compose.yaml           # 🐳 **CORE** Docker services orchestration (7 services)
├── 📄 Dockerfile                     # 🐍 Multi-stage Python environment
├── 📄 voice_agent2.py                # 🎯 Main voice agent logic
├── 📄 requirements.txt               # Python dependencies
├── 📄 .env                           # 🔒 Environment variables (YOUR SECRETS)
├── 📁 agents/                       # 🤖 Agent "Personalities" (YAML configs)
│   └── german_assistant.yaml
├── 📁 prompts/                       # 📝 Agent System Prompts (Markdown + YAML)
│   ├── prompts.yaml
│   └── default_inbound.md
├── 📁 modules/                       # **UPDATED** Core system modules
│   ├── api_server.py                # 🚀 FastAPI REST interface for outbound calls
│   ├── call_queue_manager.py        # Manages the call queue in Redis
│   ├── outbound_orchestrator.py     # Handles the logic for placing calls
│   ├── metrics_logger.py            # Metrics collection and export
│   └── sip_management.py            # **NEW** Unified SIP trunk management
├── 📄 sip_trunk_init.py              # **UPDATED** SIP trunk initialization (uses modules)
├── 📄 trunk_monitor.py               # **UPDATED** Trunk monitoring (uses modules)
├── 📁 start_scripts/                 # **NEW** Intelligent startup scripts
│   ├── start_docker.bat             # Windows doppelklick with 3 modes
│   └── start_docker.sh              # Linux/Mac doppelklick with 3 modes
├── 📁 logs/                          # Application and conversation logs
├── 📁 old/                           # **NEW** Archived redundant files
│   ├── sip_scripts/                 # 7 redundant SIP scripts (archived)
│   ├── test_scripts/                # Redundant test files
│   ├── config_files/                # Old config files
│   └── binaries/                    # Unused binaries
└── 📁 README/                        # **UPDATED** Comprehensive documentation
    ├── Masterplan_NextSteps.md      # **UPDATED** Current project status & roadmap
    ├── DOCKER_README.md             # **UPDATED** Docker configuration details
    ├── DEPLOYMENT_README.md         # Cross-platform deployment guide
    ├── START_GUIDE.md               # **NEW** Startup methods guide
    └── CLEANUP_SUMMARY.md           # **NEW** Project reorganization summary
```

---

## 🧠 Agent & Prompt Configuration (The "Brain")

The agent's behavior, voice, and intelligence are configured entirely through external files, not hardcoded. This allows for rapid iteration and creation of new agent types.

### **Agent Personalities (`/agents`)**
This directory contains YAML files, where each file defines a unique agent "personality".

- **`agents/german_assistant.yaml`**: Defines which AI components an agent uses.
  ```yaml
  name: "German Assistant"
  components:
    stt:
      provider: "azure"
      language: "de-DE"
    llm:
      provider: "openai"
      model: "azure_openai"
    tts:
      provider: "azure"
      language: "de-DE"
      voice: "de-DE-KatjaNeural"
  prompts:
    inbound: "default_inbound"
    outbound: "default_outbound"
  ```

The `voice_agent2.py` script dynamically loads an agent configuration (currently hardcoded to `german_assistant.yaml`) and assembles the required STT, LLM, and TTS components on the fly.

### **System Prompts (`/prompts`)**
This directory holds the instructional texts that guide the agent's conversations.

- **`prompts/prompts.yaml`**: A central index file that maps a `prompt_key` (e.g., `default_inbound`) to a specific prompt file and its parameters.
- **`prompts/*.md`**: The actual prompt texts, written in Markdown. This allows for clear, well-structured, and easily editable prompts.

---

## 📋 Prerequisites & Setup

### **Required Services:**
- Python 3.11+
- Docker and Docker Compose
- Azure Cognitive Services account
- Azure OpenAI access

### **Environment Configuration:**
```bash
# Copy template and configure
cp .env.example .env

# Edit .env with your credentials:
# AZURE_SPEECH_KEY=your_key_here
# AZURE_SPEECH_REGION=your_region
# AZURE_OPENAI_API_KEY=your_key_here
# AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
# AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4

# Optional Twilio integration:
# TWILIO_ACCOUNT_SID=your_sid
# TWILIO_AUTH_TOKEN=your_token
# TWILIO_PHONE_NUMBER=+1234567890
```

**Cross-Platform Note**: The SIP server is configured via the `SIP_CONFIG_BODY` environment variable in `docker-compose.yaml`. This avoids direct file volume mounts, which are a known source of errors on Windows Docker.

---

## 🐳 Docker Services Overview

| Service | Port | Purpose | Health Check |
|---------|------|---------|--------------|
| **api-server** | 8000 | REST API for outbound calls | `/health` |
| **livekit** | 7880/7881 | WebRTC media server | HTTP check |
| **redis** | 6379 | Queue & session management | PING |
| **sip-server** | 5060 | Phone call integration | Log verification |
| **sip-trunk-init** | - | Automated trunk setup | Redis check |
| **trunk-monitor** | - | System coordination | Background |
| **voice-agent** | - | AI conversation workers | Scalable (NUM_AGENTS) |

### **Service Status Verification:**
```bash
# Check all services
docker-compose ps

# Expected output: All services "Up" with "healthy" status

# Individual health checks
curl http://localhost:8000/health    # API Server
curl http://localhost:8000/docs      # API Documentation
curl http://localhost:7880           # LiveKit Server
```

---

## 📞 Making Outbound Calls

### **REST API Method (Primary):**
```bash
curl -X POST "http://localhost:8000/api/outbound-call" \
     -H "Content-Type: application/json" \
     -d '{
       "to_number": "+15005550006",
       "caller_name": "AI Assistant",
       "llm_prompt": "You are a helpful assistant calling to confirm an appointment.",
       "greeting": "Hello, this is a friendly reminder call."
     }'
```

### **Response:**
```json
{
  "status": "queued",
  "call_id": "outbound-20241219-123456-+15005550006",
  "message": "Call successfully queued for processing"
}
```

---

## 🔧 New Management Commands

### **SIP Trunk Management:**
```bash
# Using new unified module
python -m modules.sip_management ensure   # Ensure trunk exists
python -m modules.sip_management list     # List all trunks  
python -m modules.sip_management status   # Show trunk status

# CLI interface also available:
python -m modules.sip_management --help
```

### **System Management:**
```bash
# Intelligent startup
python start_optimized.py              # Smart mode
python start_optimized.py --simple     # Simple mode  
python start_optimized.py --legacy     # Legacy mode

# Service monitoring
docker-compose logs -f                 # All services
docker-compose logs -f api-server      # Specific service
docker-compose ps                      # Status overview
```

---

## ✅ System Verification & Testing

### **Service Health Checks**
After startup, verify that all services are running and healthy.
```bash
# Check status of all containers. Look for "Up" and "healthy".
docker-compose ps

# --- Individual Health Endpoints ---
# API Server: Should return {"status": "healthy"}
curl http://localhost:8000/health

# API Docs: Open in browser to see Swagger UI
# http://localhost:8000/docs

# LiveKit Server: Should return "OK"
curl http://localhost:7880

# Redis: Should return "PONG"
docker-compose exec redis redis-cli ping
```

### **Placing a Test Call**
The primary way to test the system is by placing an outbound call via the REST API.
```bash
curl -X POST "http://localhost:8000/api/outbound-call" \
     -H "Content-Type: application/json" \
     -d '{
       "to_number": "+15551234567",
       "caller_name": "AI Assistant"
     }'
```
A `200 OK` response indicates the call was successfully queued.

---

## 🎯 Key Improvements & Achievements

### **✅ Infrastructure Completed:**
- **🔧 Unified SIP Management**: 7 redundant scripts consolidated into `modules/sip_management.py`
- **🚀 Intelligent Startup**: Smart/Simple/Legacy modes with automatic fallbacks
- **📦 Cross-Platform Docker**: [Windows Docker Compose V2 bug workaround][[memory:1630037021327934692]] solved
- **🎯 Health Checks**: All services with proper startup coordination
- **📋 Project Organization**: Redundant files moved to `old/` directory
- **💻 Doppelklick Support**: Windows/Linux/Mac one-click startup maintained

### **🔄 System Status:**
- **Infrastructure**: ✅ **COMPLETED** - All Docker services running reliably
- **Cross-Platform**: ✅ **VERIFIED** - Windows/Mac/Linux compatibility
- **API Integration**: ✅ **FUNCTIONAL** - REST endpoints with documentation
- **SIP Debugging**: 🔄 **IN PROGRESS** - 403 authentication issues being resolved

---

## 🚨 Troubleshooting Guide

### **Critical Issues & Solutions**

#### ❌ **Docker Startup Issues**
**Solution**: Use Smart Mode with automatic fallbacks
```bash
python start_optimized.py              # Tries Smart → Simple → Legacy
```

#### ❌ **Windows Docker Volume Errors**
**Solution**: ✅ **ALREADY FIXED** - Environment variable configuration
- **Status**: No more "is a directory" errors
- **Verification**: All config via `SIP_CONFIG_BODY` environment variable

#### ❌ **SIP Authentication (403 Forbidden)**
**Solution**: Systematic debugging workflow available
```bash
# Check trunk status
python -m modules.sip_management status

# Verify environment variables
docker-compose exec sip-trunk-init env | grep TWILIO

# Review SIP server logs
docker-compose logs sip-server -f
```

#### ❌ **Service Coordination Issues**
**Solution**: Health checks ensure proper startup order
```bash
# Smart mode waits for service readiness
python start_optimized.py

# Manual verification
curl http://localhost:8000/health
docker-compose ps
```

### **System Commands**
```bash
# View live, aggregated logs for all services
docker-compose logs -f

# View logs for a single service (e.g., the voice agent)
docker-compose logs -f voice-agent

# Stop all services gracefully
docker-compose down

# Stop services and remove attached volumes (e.g., Redis data)
docker-compose down -v
```

### **Platform-Specific Setup**
The startup scripts are designed for cross-platform compatibility.

- **Windows**: Use `start_scripts/start_docker.bat`. Docker Desktop should use the WSL2 backend for best performance.
- **macOS / Linux**: Make the script executable (`chmod +x start_scripts/start_docker.sh`) and then run it (`./start_scripts/start_docker.sh`).

If you encounter issues, always start with a clean slate:
```bash
docker-compose down --rmi all -v
docker system prune -af
python start_optimized.py
```

---

## 🔍 Platform-Specific Information

### **Windows Development** ✅
- **Docker Desktop**: Use WSL2 backend for best compatibility
- **Startup**: Doppelklick `start_scripts/start_docker.bat`
- **PowerShell**: All commands compatible
- **Known Issues**: Volume mounting solved via environment variables

### **Mac Development** ✅
- **Docker Desktop**: Standard installation works perfectly
- **Startup**: Doppelklick `start_scripts/start_docker.sh` 
- **M1/M2 Macs**: ARM64 compatible images used
- **File Paths**: Full compatibility with all configurations

### **Linux Development** ✅
- **Docker**: Native Docker or Docker Desktop
- **Startup**: Execute `start_scripts/start_docker.sh`
- **Permissions**: May need Docker group adjustments
- **Performance**: Best performance (native containers)

---

## 🎯 Production Deployment

### **Scaling Configuration:**
```bash
# Scale voice agents based on call volume
NUM_AGENTS=5 docker-compose up -d voice-agent

# Resource recommendations:
# - Memory: 8GB for 25 concurrent calls
# - CPU: 4 cores for 25 concurrent calls
# - Network: UDP ports 50000-50100 open
```

### **Environment Management:**
- **Development**: Local Docker with `.env` files
- **Staging**: Environment variable injection via CI/CD
- **Production**: Secret management system (Azure Key Vault, AWS Secrets)

---

## 📊 Monitoring & Analytics

### **Health Monitoring:**
```bash
# Comprehensive system status
curl http://localhost:8000/health
# Returns: {"status": "healthy", "services": {...}}

# Individual service checks
curl http://localhost:7880           # LiveKit: "OK"
docker-compose exec redis redis-cli ping  # Redis: "PONG"
docker-compose ps                    # All services: "Up (healthy)"
```

### **Metrics Collection:**
```bash
# API metrics (if implemented)
curl http://localhost:8000/metrics

# Resource monitoring
docker stats --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}"

# Log analysis
docker-compose logs --since 1h | grep -E "(error|warning|403)"
```

---

## 🔄 Project Evolution Summary

### **Major Problems Solved:**

1. **✅ Cross-Platform Docker Compatibility**: 
   - **Problem**: Windows Docker Compose V2 mounting files as directories
   - **Solution**: Environment variable configuration with `SIP_CONFIG_BODY`
   - **Impact**: Universal Windows/Mac/Linux deployment

2. **✅ Code Organization & Maintainability**:
   - **Problem**: 7 redundant SIP scripts scattered across project
   - **Solution**: Unified `modules/sip_management.py` with CLI interface
   - **Impact**: Single source of truth, easier testing and maintenance

3. **✅ Startup Complexity & Reliability**:
   - **Problem**: Manual Docker commands, no health coordination
   - **Solution**: Intelligent startup scripts with 3 modes and fallbacks
   - **Impact**: One-click startup with automatic error recovery

4. **✅ Documentation & Knowledge Management**:
   - **Problem**: Scattered, outdated documentation
   - **Solution**: Centralized README structure with current status
   - **Impact**: Clear project understanding and onboarding

---

## 📚 Documentation Resources

### **Primary Documentation:**
- **[Masterplan_NextSteps.md](README/Masterplan_NextSteps.md)**: Current status & debugging workflow
- **[DOCKER_README.md](README/DOCKER_README.md)**: Complete Docker configuration
- **[START_GUIDE.md](README/START_GUIDE.md)**: Startup methods comparison
- **[DEPLOYMENT_README.md](README/DEPLOYMENT_README.md)**: Cross-platform deployment

### **External Resources:**
- **[LiveKit SIP Documentation](https://docs.livekit.io/sip/)**: Official SIP integration guides
- **[Twilio SIP Trunking](https://www.twilio.com/docs/sip-trunking)**: Provider configuration
- **[Azure Speech Services](https://docs.microsoft.com/azure/cognitive-services/speech-service/)**: STT/TTS setup
- **[Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/)**: LLM integration

---

**Current Status:** 🔄 **INFRASTRUCTURE COMPLETED - SIP DEBUGGING IN PROGRESS**

**Next Steps:** Complete 403 authentication debugging → End-to-end call testing → Production optimization

---

*Built with ❤️ using LiveKit, Azure AI Services, and modern cloud infrastructure*

**Key Achievement**: Comprehensive system architecture with cross-platform compatibility, intelligent startup options, and production-ready Docker orchestration.
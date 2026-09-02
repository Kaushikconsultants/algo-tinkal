import React from 'react';

function App() {
  return (
    <div className="min-h-screen p-8">
      <header className="mb-8 flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-primary to-purple-400">
            Dhan Algo Terminal
          </h1>
          <p className="text-gray-400 mt-1">Real-time trading \u0026 execution platform</p>
        </div>
        <div className="flex items-center gap-4">
          <span className="flex items-center gap-2">
            <span className="w-3 h-3 rounded-full bg-success animate-pulse"></span>
            System Live
          </span>
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* P\u0026L Overview Card */}
        <div className="glass-card p-6 col-span-1 md:col-span-2">
          <h2 className="text-xl font-semibold mb-4">Live Performance</h2>
          <div className="h-64 flex items-center justify-center border border-dashed border-white/20 rounded-xl bg-black/20">
            <p className="text-gray-500">Equity Curve Chart (Pending Data Integration)</p>
          </div>
        </div>

        {/* Strategy Control Card */}
        <div className="glass-card p-6">
          <h2 className="text-xl font-semibold mb-4">Active Strategies</h2>
          
          <div className="space-y-4">
            <div className="p-4 bg-white/5 rounded-xl border border-white/10 flex justify-between items-center">
              <div>
                <h3 className="font-medium text-primary">MA Crossover</h3>
                <p className="text-sm text-gray-400">NIFTY 50 • 10/30 Period</p>
              </div>
              <div className="w-12 h-6 bg-success/20 rounded-full p-1 cursor-pointer">
                <div className="w-4 h-4 bg-success rounded-full transform translate-x-6"></div>
              </div>
            </div>

            <div className="p-4 bg-white/5 rounded-xl border border-white/10 flex justify-between items-center opacity-60">
              <div>
                <h3 className="font-medium">Options Straddle</h3>
                <p className="text-sm text-gray-400">BANKNIFTY • 9:20 AM</p>
              </div>
              <div className="w-12 h-6 bg-gray-600 rounded-full p-1 cursor-pointer">
                <div className="w-4 h-4 bg-gray-400 rounded-full"></div>
              </div>
            </div>
          </div>
        </div>

        {/* Live Logs Card */}
        <div className="glass-card p-6 col-span-1 md:col-span-3">
          <h2 className="text-xl font-semibold mb-4">Execution Logs</h2>
          <div className="bg-black/40 rounded-xl p-4 h-48 overflow-y-auto font-mono text-sm space-y-2">
            <div className="text-gray-400">[10:15:00 AM] System initialized. DhanHQ SDK connected.</div>
            <div className="text-primary">[10:15:05 AM] Loaded 1342 instrument definitions.</div>
            <div className="text-success">[10:16:00 AM] MA_Crossover started listening to NIFTY 50 feed.</div>
            <div className="text-gray-400 animate-pulse mt-4">_ Waiting for signals...</div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;

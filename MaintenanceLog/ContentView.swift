//
//  ContentView.swift
//  MaintenanceLog
//
//  Created by Y. Khusanova on 13.02.26.
//

import SwiftUI
import SwiftData

struct ContentView: View {
    @Query private var entries: [LogEntry]

    var body: some View {
        Text("Spaceship Home Maintenance Log: ")
        ForEach(entries){
            entry in Text(entry.content)
        }
    }
}

#Preview {
    let container = try! ModelContainer(for: LogEntry.self, configurations: ModelConfiguration(isStoredInMemoryOnly: true))
    
    container.mainContext.insert(LogEntry.waterPlants)
    container.mainContext.insert(LogEntry.vacuum)
    container.mainContext.insert(LogEntry.cleanDishWasherFilter)
    
    return ContentView()
        .modelContainer(container)
}
